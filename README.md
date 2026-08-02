# Python Learning Lab

A personal sandbox for learning Python — language fundamentals, libraries, web APIs, networking, and AI agents.

This repo used to be called **python-playground**. It is now organized by topic so experiments stay easy to find.

## Layout

| Folder | What lives here |
|--------|-----------------|
| `fundamentals/` | Language basics, OOP/DSA, decorators, generators, async, OAuth sketch |
| `libraries/` | One-off library scratchpads (`lib_*.py`), pandas, SQLAlchemy demos |
| `web/` | Flask & FastAPI tutorials, inventory CRUD app, Plotly Dash |
| `ai/` | LangChain, LangGraph, MCP, Hugging Face / Ollama, Dockerized MCP server |
| `networking/` | Sockets and packet-sniffing experiments |
| `testing/` | `pytest` and `unittest` practice |
| `challenges/` | Small algorithm drills |
| `apps/` | Personal utilities (e.g. German vocab quiz) |
| `tools/` | `uv` project bootstrap, package inspector, embedded/serial notes |
| `notes/` | Quick reference snippets (git commits, content types) |

## Notable projects

- **`web/api/fastapi/project1`** — FastAPI server + client (NJ→NY delivery demo)
- **`web/api/fastapi/project2`** — Gemini chat API with JWT auth and throttling
- **`web/inventory-app`** — FastAPI + SQLAlchemy + Jinja user CRUD UI
- **`ai/langchain/project1`** — Local Ollama RAG over restaurant reviews
- **`ai/langchain/pdf-qa`** — Chainlit PDF Q&A
- **`ai/langgraph/project2`** — Multi-source research agent graph
- **`ai/mcp/`** — MCP servers/clients (stdio, SSE, HTTP) vs classic function-calling
- **`ai/docker-mcp`** — MCP calculator server packaged with Docker
- **`libraries/sqlalch`** / **`sqlalch2`** — Flask vs FastAPI + SQLAlchemy progression
- **`apps/mygerman`** — Excel-based German vocabulary quiz

## Getting started

Most folders are self-contained. Prefer running from inside the project directory.

### Prerequisites

- Python 3.9+ (several projects pin 3.12 via `.python-version`)
- [`uv`](https://github.com/astral-sh/uv) or `pip`
- Docker (only for `ai/docker-mcp` and the Azure PDF-QA image)

### Clone

```bash
git clone https://github.com/iliarusskikh/Python-Learning-Lab.git
cd Python-Learning-Lab
```

### Run a project

```bash
# Example: FastAPI Gemini project
cd web/api/fastapi/project2
pip install -r requirements.txt   # or: uv sync / uv pip install -r requirements.txt
uvicorn main:app --reload
```

```bash
# Example: uv tooling sandbox
cd tools/uv
uv sync
uv run main.py
```

Projects that call external APIs expect keys in a local `.env` (never committed). Typical names: `OPENAI_API_KEY`, `GEMINI_API_KEY`, `PINECONE_API_KEY`, `AZURE_OPENAI_*`.

## Notes

- Scripts are learning experiments, not production code. Demo secrets in older Flask/OAuth samples are intentional placeholders.
- Each multi-file project keeps its own `requirements.txt` or `pyproject.toml`.
- Commit style cheat-sheet: see `notes/commit-standard.md`.
