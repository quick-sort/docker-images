# Use the official vllm image for gpu with Volta、Turing、Ampere、Ada Lovelace、Hopper、Blackwell architecture (7.0 <= Compute Capability <= 12.0)
# Compute Capability version query (https://developer.nvidia.com/cuda-gpus)
# support x86_64 architecture and ARM(AArch64) architecture
FROM vllm/vllm-openai:v0.11.2

# Install libgl for opencv support & Noto fonts for Chinese characters
RUN apt-get update && \
    apt-get install -y \
        fonts-noto-core \
        fonts-noto-cjk \
        fontconfig \
        libgl1 && \
    fc-cache -fv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# For China area
# ENV PIP_INDEX_URL=https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/

# Install mineru latest
RUN python3 -m pip install -U 'mineru[core,vlm]==3.1.6' --break-system-packages && \
    python3 -m pip cache purge

# Download models and update the configuration file
# For China area
# ENV MINERU_MODEL_SOURCE=modelscope
RUN /bin/bash -c "mineru-models-download -s huggingface -m all"

ENV MINERU_MODEL_SOURCE=local
VOLUME ["/vllm-workspace/output"]
# Set the entry point to activate the virtual environment and run the command line tool
ENTRYPOINT ["/bin/bash", "-c", "exec \"$@\"", "--"]
