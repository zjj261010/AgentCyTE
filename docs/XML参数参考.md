# AgentCyTE XML 参数全参考(构造拓扑时各参数作用)

> 来源：逐个核对 `core_topo_gen/parsers/*.py` 解析器 + 矩阵实测（哪些组合会 RUNNING / 卡 CONFIGURATION）。
> 形态：离线环境 core 容器内 + agentcyte 宿主机。配套模板见 `docs/examples/scenario-offline-max.xml`。

---

## 0. 根元素与通用 item 属性

### `<Scenarios>` / `<Scenario>`
| 属性 | 类型 | 作用 | 备注 |
|:--|:--|:--|:--|
| `name` | string (必需) | 会话/场景名，CLI `--scenario` 用它选中 | `scenario_total_nodes` 只读/信息性，解析时**不用它做数量硬上限** |
| `scenario_total_nodes` / `base_nodes` | int | 数量**密度基线**（不是上限），决定 Node Info 的 host 池规模 | 实测：它和最终生成节点数通常**不一致**（详情见 FAQ Q3） |

### `<BaseScenario filepath=""/>`
- 一个 CORE 会话 XML 作为**基础布局**（可选）。`filepath=""` = 空=不基于已有布局，纯按 section 生成。

### `<item>` 通用属性（贯穿各 section，XSD 允许全集、未用到的忽略）
| 属性 | 类型 | 作用 |
|:--|:--|:--|
| `selected` | string | 该行选中的**类型/角色/协议名**（随 section 不同，见各节） |
| `v_metric` | `Count` / `Weight` | **分配度量**：`Count` = 绝对数量（additive），`Weight` = 按权重比例分配密度池 |
| `v_count` | int | `v_metric="Count"` 时的绝对数量 |
| `factor` | float | `v_metric="Weight"` 时的权重因子 |
| `v_type` / `v_vector` | string | vuln 的 Type/Vector 分类 |
| `v_name` / `v_path` | string | vuln 的 Specific 名称与 compose 路径 |

> **`v_metric` 是数量语义的核心开关**：`Count` 是「加法项」（`count_items`），`Weight` 是「比例项」（`weight_items`，按 `factor` 从密度池分）。解析器先收集 `count_map` 与 `weight_items`，再 `compute_role_counts` 合成最终 `role_counts`。

### `<section>` 级属性（功能型 + 规划元数据型）

每个 `<section>` 上除了 `name`，还能挂两类属性——**功能型**（解析器直接读到并影响拓扑生成）和**规划元数据型**（UI 写回做 round-trip，CLI 在 report 里回显/校验，**不直接决定生成**）：

| 属性 | 类型 | 应用 section | 作用 | 分类 |
|:--|:--|:--|:--|:--|
| `density` | float 或 int | Routing / Services / Traffic / Vulnerabilities / Segmentation | **密度**：`≤1` 按比例、`>1` 按绝对值（语义随 section 不同） | **功能型** |
| `base_nodes` | int | Node Information | host 密度池基数（`density_base`），按比例分池 | **功能型** |
| `density_count` | int | Node Information | `base_nodes` 的旧别名（legacy） | **功能型** |
| `total_nodes` | int | Node Information | 该 section「总节点」声明（历史字段，Node Info 池取数的降级来源之一） | **功能型** |
| `additive_nodes` | int | Node Information | Count 行合计（=`base` 外再叠加的绝对数） | **规划元数据** |
| `combined_nodes` | int | Node Information | `base_nodes + additive_nodes` 合计 | **规划元数据** |
| `weight_rows` | int | Node Info / Routing / Services / Traffic / Vulnerabilities / Segmentation | Weight 行数（门控：`weight_rows>0` 才收 Weight item） | **规划元数据** |
| `count_rows` | int | 同上 | Count 行数（门控） | **规划元数据** |
| `weight_sum` | float | 同上 | Weight 因子原始和（未归一化） | **规划元数据** |
| `explicit_count` | int | Routing / Vulnerabilities | 绝对行合计（additive） | **规划元数据** |
| `derived_count` | int | Routing / Vulnerabilities | 密度推导量 | **规划元数据** |
| `total_planned` | int | Routing / Vulnerabilities | `explicit_count + derived_count` | **规划元数据** |

**要点**：
- **功能型**必须写对——`base_nodes`/`density` 直接影响「建多少节点/多密」。**规划元数据是可选回显字段**：写不写、写得对不对，**不影响拓扑生成**，但 CLI 会在 report/规划 JSON 里以 `plan_*_*` 键回显（`cli.py` 里 `plan_node_additive_nodes`、`plan_routing_explicit`…），供前后端对账。
- `weight_rows` 特殊：**它决定是否启用 Weight 门控**（`node_info.py`：只有 section 的 `weight_rows` 属性存在时，Weight item 的 `factor` 才被收集）。如果你在 Node Info 写了 Weight item，应带 `weight_rows` 反映行数。
- 与「离线黄金规则」冲突时：功能型里 `density` 可自由调（不影响 RUNNING）；规划元数据随便写与否都不卡——真正影响卡 CONFIG 的是 `item` 的 `Wireless` 角色、`Traffic`/`Segmentation` section（见 FAQ Q4/Q5）。

**实例**（一个同时带两类的 section）：
```xml
<section name="Routing" density="1.0"          <!-- 功能型 -->
         explicit_count="2" derived_count="0" total_planned="2"  <!-- 元数据 -->
         weight_rows="1" count_rows="1" weight_sum="1.000">
  <item .../>
</section>
```

---

## 1. `<section name="Node Information">` —— 角色与数量
**作用：定义参与节点的角色种类与数量，直接决定「建多少台什么节点」。**

### section 属性
| 属性 | 作用 |
|:--|:--|
| `base_nodes` / `density_count` / `total_nodes` | host 密度池基数（`density_base`，解析优先级依次取） |
| `weight_rows` / `count_rows` | 记录该 section 里 Weight 行数/Count 行数（规划元数据，可选） |

### item（`selected` = 角色名）
| selected | 映射到 CORE 节点 | 构造拓扑时的作用 |
|:--|:--|:--|
| `Router` | DEFAULT + `model=router` + zebra/IPForward | 建**真路由器**（需 Routing section 配合，否则退化为普通 PC） |
| `Switch` | SWITCH 节点 | 建交换机，作为网段汇聚点 |
| `Hub` | HUB 节点 | 建集线器（实测**不影响 RUNNING**） |
| `Workstation` | DEFAULT + `model=PC` | 建主机（默认 `model=PC`、DefaultRoute/SSH 服务由 Services 决定） |
| `Wireless` | WIRELESS_LAN 节点 | 建无线接入点（实测**会卡 CONFIGURATION，离线请勿用**） |
| 其它 | DEFAULT PC | 未识别角色一律回落为普通 PC |

**双度量**：可在同一 section 混用 `v_metric="Count"` 与 `v_metric="Weight"`。例如：
```xml
<item selected="Router" v_metric="Count" v_count="2"/>
<item selected="Workstation" v_metric="Count" v_count="5"/>
<item selected="Workstation" v_metric="Weight" factor="0.6"/>   <!-- 另有 0.4 → 0.6+0.4=1.0 全池 -->
```
- `Count`（additive）：`v_count` 个该角色**必定加进来**（不受密度限）。
- `Weight`（proportional）：占 density 池的比例补该角色数量。
- ⚠️ **实测边界**：Weight + Switch/Hub 组合会让最终节点结构 >23 时**卡 CONFIGURATION**（见 FAQ Q5）。离线最大模板里统一用 Count 最稳。

---

## 2. `<section name="Routing">` —— 路由协议与网段
**作用：声明路由协议、路由器数量、路由器↔交换机挂接策略。** 有该 section → 走 `build_segmented_topology`（建真路由器+多网段）；无该 section → 走 `build_star`（扁平，路由器沦为普通 PC、无 zebra/OSPF）——**这是"真路由器"的开关**。

### section 属性：`density` — 路由密度（0~1 或绝对量）

### item（`selected` = 协议）
| selected | 作用 |
|:--|:--|
| `OSPFv2` / `OSPFv3` / `RIP` / `BGP`… | 路由协议，附加到路由器服务的 `ospf_*/zebra/ip_forward` |

### Routing 专属「挂接策略」参数（决定网段拓扑形态）
| 参数 | 作用 | 实测备注 |
|:--|:--|:--|
| `r2r_mode` | 路由器↔路由器连接策略（`Uniform/NonUniform/Exact/Min`） | `r2r_edges` 配合（Exact 时目标边数） |
| `r2r_edges` | 每路由与其他路由的期望边数（Exact 模式下） | |
| `r2s_mode` | 路由器↔**交换机** host 聚合策略（`Exact/NonUniform/aggregate/ratio`） | `Exact` = 精确（`r2s_edges` 控交换机数） |
| `r2s_edges` | Exact 模式下每路由挂的交换机数 | **直接决定交换机数量**（≈ 路由数 × edges） |
| `r2s_hosts_min` / `r2s_hosts_max` | 每生成的交换机下限/上限主机数（NonUniform 分组） | 实测：Routing 全部高级参数（含这些）**不影响 RUNNING** |

**数量核算**（见 FAQ Q3）：路由器 =`v_count`（additive）；交换机 ≈ `routers × r2s_edges`；host 按密度往各网段补齐 → 总节点常超出 base。

---

## 3. `<section name="Services">` —— 节点服务
**作用：给主机/节点分配 CORE 服务**（`model=PC` 的服务集由这里定）。

### item（`selected` = 服务名）
| selected | 构造拓扑时的作用 | 实测 |
|:--|:--|:--|
| `SSH` | 主机加 SSH 服务（可进终端） | ✅ RUNNING |
| `DefaultRoute` | 主机加默认路由（连到网关/路由） | ✅ RUNNING |
| `DHCP` | 分配 DHCP 服务 | ✅ RUNNING（离线无 docker 也不影响，DHCP 是 CORE 自身服务） |
| `zebra` / `IPForward` / `ospf_*` | 路由侧服务（Router 默认就有，此处可覆盖） | ✅ |
| 其它 CORE 服务名 | 按名附加 | |

---

## 4. `<section name="Traffic">` —— 流量生成
**作用：声明流量模式与速率**（`pattern/rate_kbps/period_s/jitter_pct/content`），CLI 生成流量脚本写 `receivers/senders`。

⚠️ **实测：Traffic section 一出现，`start_session` 提前返回（~1–2s），会话停 CONFIGURATION。离线请勿用**（FAQ Q4）。

| 参数 | 作用 |
|:--|:--|
| `pattern` | `continuous/periodic/burst/poisson/ramp` |
| `rate_kbps` | 速率（kbps） |
| `period_s` | 周期（秒，默认 10） |
| `jitter_pct` | 抖动 0–100 |
| `content` / `content_type` | 内容（text/photo/audio/video） |

---

## 5. `<section name="Events">` —— 事件脚本
**作用：声明事件脚本**（信息性标注，规划时写入，当前 CLI 不真正执行）。
`<item selected="startup" script_path="..."/>` — `script_path` 指向脚本。
实测：**Events 不影响 RUNNING**（但请保留时给真实脚本路径或留空均可）。

---

## 6. `<section name="Vulnerabilities">` —— 漏洞标注 / docker
**作用：给主机打 CVE 标签、可选生成 docker 节点。**

| item selected | 作用 | 离线可用性 |
|:--|:--|:--|
| `Type/Vector` | 按 `v_type`/`v_vector` 分类打标签 | ✅ **可用**（只打标签，不建容器） |
| `Random` | 随机挑 vuln | ✅ **可用** |
| `Specific` | 解析 `v_name`/`v_path`（compose）→ **建 DOCKER 节点** | ⚠️ **慎用**：core 容器内若无 docker（socket/dind），DOCKER 节点起不来 → 卡会话 |

section 属性：`density`、`explicit_count`/`derived_count`/`total_planned`（规划元数据）。

---

## 7. `<section name="Segmentation">` —— 分段
**作用：声明分段（VLAN/网段子组）语义**，`selected` 为分段名，`v_metric`/`v_count`/`factor` 控数量。

⚠️ **实测：Segmentation section 卡 CONFIGURATION。离线请勿用**（FAQ Q4）。

---

## 8. `<section name="Notes">` —— 说明
```xml
<section name="Notes"><notes>自由文本</notes></section>
```
仅注释，不参与拓扑。

---

## 离线形态黄金规则（推荐值）
| 参数 | 推荐 | 原因 |
|:--|:--|:--|
| `v_metric` | 用 **Count**（别用 Weight 双度量） | Weight+Switch/Hub >23 节点卡 CONFIG |
| `Wireless` 角色 | **不用** | 卡 CONFIG |
| `Traffic` / `Segmentation` | **不用** | 卡 CONFIG |
| vuln `Specific` | **不用**（只用 Type/Vector + Random） | 需容器内 docker |
| 其余（Router/Switch/Hub、Routing 全参数、Services、Events、vuln Type/Vector） | 全部保留 | 实测 RUNNING |

→ 完整可用模板：`docs/examples/scenario-offline-max.xml`（23 节点 RUNTIME 实测）。

---

*环境：AgentCyTE venv 离线包 + 宿主 core-daemon / core 容器 9.2.1 + core-http-bridge。*
