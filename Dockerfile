# AgentCyTE Web UI —— 独立容器, 隔离部署
# build context = 仓库根 (与 webapp/、core_topo_gen/、main.py 同级)
# 镜像源: 阿里云 PyPI (pypi.tuna 在此机器被拒)
# gRPC(CORE) 为可选依赖: 容器内不装 core 包 → CORE_GRPC_AVAILABLE=False,
#   Web UI 上传/生成/预览/报告可用; 推送真实 CORE 需单独挂载宿主 core 包
FROM python:3.10-slim

WORKDIR /app

# 1. 系统基础: tzdata/CA 证书(避免 lxml 从 TLS 源下载实体时证书缺失)
RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates tzdata \
    && rm -rf /var/lib/apt/lists/*

# 2. 先装依赖(利用层缓存; 用阿里云 PyPI 镜像加速)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ \
        -r /app/requirements.txt

# 3. 复制整个仓库(保持 webapp/ + core_topo_gen/ + data_sources/ 结构)
COPY . /app

# 4. vendor/core: 内置独立 CORE 客户端库(纯 Python, 来自宿主 CORE venv)
#    目的: 容器内 CORE_GRPC_AVAILABLE=True, 可推拓扑; 实际连接仍指向外部 CORE daemon
COPY vendor/core /app/vendor/core

# 5. 容器内可写目录(uploads/outputs/reports 由 app 在 /app 下创建)
RUN mkdir -p /app/uploads /app/outputs /app/reports

# 6. PYTHONPATH 加入 vendor, 使容器 import core 命中内置客户端库
ENV PYTHONPATH=/app/vendor

EXPOSE 9090

ENV CORETG_HOST=0.0.0.0
ENV CORETG_PORT=9090
# 不设 debug, 生产模式运行
ENV CORETG_DEBUG=

CMD ["python", "main.py"]