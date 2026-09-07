# 代码修改清单（AgentCyTE 离线包 vs 上游 AnantaaKotal/AgentCyTE）

> 对比对象：
> - **离线包部署版**：`/tmp/agentcyte-offline-build/agentcyte`（venv 形态离线包内源码，HEAD `3f4b269`）
> - **上游原始版**：`https://github.com/AnantaaKotal/AgentCyTE.git`（clone 后核对）
>
> 方法：逐文件 sha256 比对。上游独有文件 0 个；新增 255 个（部署相关）；内容改动 5 个文件 6 处；完全相同 214 个文件。

---

## 一、功能源码修改：5 个文件、6 处（全部是 bug 修复）

### 1. `main.py`（1 处）

| 项 | 内容 |
|:--|:--|
| 行号 | line 29-30（`app.run` 调用处） |
| 原版 | `app.run(host=default_host, port=port, debug=debug)` |
| 修改 | `app.run(host=default_host, port=port, debug=debug, threaded=True)` |
| 目的 | Werkzeug 默认**单线程**，一个阻塞请求卡死整页（麒麟上 curl `000`）；加 `threaded=True` 支持并发 |

### 2. `webapp/app_backend.py`（2 处）

| 项 | 内容 |
|:--|:--|
| 位置① | import 区，line 10-20 |
| 原版① | `import threading` … `import csv`（无线程池） |
| 修改① | 插入 `from concurrent.futures import ThreadPoolExecutor`，定义 `_REUSE_ASYNC_POOL = ThreadPoolExecutor(max_workers=4, thread_name_prefix="finalizer")` |
| 位置② | 异步 run finalizer 提交处，line ~4972-4975 |
| 原版② | `t = threading.Thread(target=_wait_and_finalize_async, args=(run_id,), daemon=True)` `t.start()`（每 run 新建 daemon 线程、不回收） |
| 修改② | `_REUSE_ASYNC_POOL.submit(_wait_and_finalize_async, run_id)`（复用 4 线程池） |
| 目的 | 修麒麟首次部署「线程无法创建」：旧实现线程堆积撞 pids / `vm.max_map_count` 上限 |

### 3. `core_topo_gen/builders/topology.py` `build_star_from_roles`（2 处）

| 项 | 内容 |
|:--|:--|
| 位置① | 函数签名，line 574-581 |
| 原版① | `..., docker_slot_plan: Optional[Dict[...]] = None):`（无 `layout_density` 参数） |
| 修改① | 末尾追加 `layout_density: str = "normal"` |
| 位置② | 函数内半径计算 + 返回语句，line ~604-607、~790-793 |
| 原版② | `radius = 250`（固定）；`return session, switch, node_infos, service_assignments, docker_by_name`（裸 `switch` 对象） |
| 修改② | `radius = 170 if layout_density == "compact" else (330 if ... == "spacious" else 250)`（随密度）；`return session, [switch], node_infos, ...`（list 形态，与 `build_multi_switch_topology` 对齐） |
| 目的 | 修 TypeError（缺参数）；修 `len(switch)` 崩溃（调用侧期望 list） |

### 4. `pyproject.toml`（1 处）

- `dependencies` 中 `lxml==6.0.0` → `lxml==6.1.2`
- 原因：`lxml==6.0.0` **在 PyPI 不存在**，安装/构建必失败

### 5. `requirements.txt`（整文件重写）

原版 6 行 → 全量锁定 16 条（直接依赖 + 传递依赖闭包）：

| 项 | 原版 | 当前离线包 |
|:--|:--|:--|
| lxml | `lxml==6.0.0`（不存在） | `lxml==6.1.2` |
| Web 栈 | `Flask==3.0.3` `Werkzeug==3.0.3` `PyYAML==6.0.2` `psutil==5.9.8` | 保留 |
| 内置 CORE 客户端依赖 | —— | `+ grpcio==1.69.0` `+ protobuf==5.29.3` `+ netaddr==0.10.1`（与宿主 CORE venv 对齐） |
| 传递依赖闭环 | —— | `+ blinker==1.9.0` `+ click==8.5.0` `+ exceptiongroup==1.3.1` `+ Jinja2==3.1.6` `+ itsdangerous==2.2.0` `+ MarkupSafe==3.0.3` `+ packaging==26.3` `+ typing_extensions==4.16.0` |
| 测试工具 | `pytest>=8.0.0` | **删除**（运行包不含测试/开发依赖） |

---

## 二、新增文件（非源码 / 部署相关）：255 个

- **内置 CORE 客户端 `vendor/core/`（≈240 个）**
  - 纯 Python 包，来自宿主 CORE 9.2.1（`COREDPY_VERSION = "9.2.1"`）
  - 作用：使 `from core.api.grpc.client import CoreGrpcClient` 在脱离容器的 venv 里 import 成功；`PYTHONPATH=<包根>/vendor` 即生效
  - 兼容性：`core/api/grpc/core_pb2.py` 等协议文件与宿主 daemon **md5 字节级一致** → 版本 patch 差异（9.2.0 vs 9.2.1）无影响
- **部署脚本 4 个**：`install.sh`（建 venv + 全离线装 wheel `--no-index --find-links`）、`run.sh`（设 `PYTHONPATH=vendor` + 透传 `CORETG_PORT / CORE_HOST / CORE_PORT` + 启动）、`stop.sh`、`status.sh`
- **容器构建**：`Dockerfile`、`.dockerignore`（保留容器化能力）
- **`安装说明.md`**：部署手册（含麒麟 V10 排障 §6）
- **本文档**：`docs/代码修改清单-vs-上游.md`

---

## 三、未修改文件：214 个（与上游字节级一致）

`webapp/` 其余、`core_topo_gen/` 其余、`docs/`（原 openapi.yaml 等）、`validation/`、`data_sources/`、`tests/`、`difficulty_analysis/`、`nginx/`、`envoy/`、`scripts/`，以及顶层 `README.md`、`Makefile`、`API.md`、`sync.sh`、`sample.xml`、`config2scen_core_grpc.py` 等 —— **sha256 全部相同，零改动**。

---

## 总结

> 离线包 = 上游 AgentCyTE + 5 文件 6 处 bug 修复（麒麟 2 处 + 源 bug 3 处 + lxml 版本）+ 内置 CORE 客户端（vendor/core）+ 离线部署脚本/说明；
> `requirements.txt` 由 pytest 开发集改为**全量锁定运行闭包（16 依赖）**；
> 上游源码功能**无任何删除**。
