# MinerU

Document parsing service based on [MinerU](https://github.com/opendatalab/MinerU). Supports PDF, images, DOCX, PPTX, and XLSX.

Image: `ghcr.io/quick-sort/mineru:3.1.6`

## Compose Files

| File | Requirement |
|---|---|
| `docker-compose.yaml` | NVIDIA GPU |
| `docker-compose.cpu.yaml` | CPU only |

## Services

Each service is gated by a [profile](https://docs.docker.com/compose/how-tos/profiles/). Start only what you need.

| Profile | Service | Port | Description |
|---|---|---|---|
| `api` | mineru-api | 8000 | REST API for file parsing |
| `openai-server` | mineru-openai-server | 30000 | OpenAI-compatible server |
| `router` | mineru-router | 8002 | Load-balancing router across multiple workers |
| `gradio` | mineru-gradio | 7860 | Web UI |

## Quick Start

```bash
# GPU - start the API service
docker compose --profile api up -d

# CPU - start the API service
docker compose -f docker-compose.cpu.yaml --profile api up -d

# Start the web UI
docker compose --profile gradio up -d

# Start multiple services
docker compose --profile api --profile gradio up -d

# Stop
docker compose --profile api down
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/file_parse` | Synchronous parse (upload and wait for result) |
| POST | `/tasks` | Submit async parse task |
| GET | `/tasks/{task_id}` | Check task status |
| GET | `/tasks/{task_id}/result` | Get task result |

API docs available at `http://<host>:<port>/docs`.

## Test Client

```bash
# Sync parse
python test_client.py document.pdf

# Async parse
python test_client.py document.pdf --async

# Specify backend (default: pipeline)
python test_client.py document.pdf --backend pipeline
```

Available backends:
- `pipeline` — general purpose, multi-language, no GPU required
- `vlm-auto-engine` — high accuracy, requires GPU, Chinese/English only
- `hybrid-auto-engine` — high accuracy, requires GPU, multi-language

## GPU Configuration

In `docker-compose.yaml`, adjust GPU allocation per service:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          device_ids: ["0"]  # Multiple GPUs: ["0", "1"]
          capabilities: [gpu]
```

If running into VRAM issues, uncomment and tune `--gpu-memory-utilization` (e.g. `0.5` or lower).
