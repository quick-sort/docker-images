# Docker Images

Pre-built Docker images published to GitHub Container Registry (ghcr.io). Images are automatically built and pushed via GitHub Actions when changes are merged to `main`.

## Images

| Image | Pull | Description |
|---|---|---|
| [mineru](./mineru) | [![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fquick--sort%2Fmineru-blue?logo=docker)](https://ghcr.io/quick-sort/mineru) | [MinerU](https://github.com/opendatalab/MinerU) document parsing service (GPU) based on [vllm-openai](https://hub.docker.com/r/vllm/vllm-openai) |
| [mineru-cpu](./mineru-cpu) | [![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fquick--sort%2Fmineru--cpu-blue?logo=docker)](https://ghcr.io/quick-sort/mineru-cpu) | [MinerU](https://github.com/opendatalab/MinerU) document parsing service (CPU) based on [vllm-openai-cpu](https://hub.docker.com/r/vllm/vllm-openai-cpu) |
| [tinyproxy](./tinyproxy) | [![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fquick--sort%2Ftinyproxy-blue?logo=docker)](https://ghcr.io/quick-sort/tinyproxy) | Lightweight HTTP/HTTPS proxy server |

## How It Works

Each subdirectory contains a `Dockerfile` and a `version` file. When a change is pushed to `main`, the CI workflow detects which directories were modified, reads the `version` file for the tag, and builds/pushes the image to `ghcr.io/quick-sort/<folder>:<version>`.

## Pull

```bash
# GPU
docker pull ghcr.io/quick-sort/mineru:3.1.6

# CPU
docker pull ghcr.io/quick-sort/mineru-cpu:3.1.6

# Tinyproxy
docker pull ghcr.io/quick-sort/tinyproxy:1.11.3
```

## Adding a New Image

1. Create a new directory with a `Dockerfile` and a `version` file.
2. Push to `main` — the CI will automatically build and publish it.
