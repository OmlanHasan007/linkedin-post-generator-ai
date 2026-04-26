# 🚀 AI LinkedIn Post Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A full-stack AI application that generates professional, structured LinkedIn posts from a single topic input.**  
Built with FastAPI · LangChain · OpenAI-compatible LLMs · Nginx · Docker

</div>

---

## ✨ Features

- 🤖 AI-generated LinkedIn posts using LangChain + any OpenAI-compatible LLM
- 🌍 Multi-language support (English, Spanish, German, French, Hindi, Bangla)
- 🎨 Tone selector — Professional, Inspirational, Casual, Thought Leadership
- 📦 Structured JSON output (Title · Content · Hashtags · Call-to-Action)
- ⚡ FastAPI backend with interactive Swagger docs
- 🐳 One-command Docker deployment
- 🔒 Secure by default — non-root Docker user, security headers via Nginx

---

## 🏗️ Architecture

```
User (Browser)
     │
     ▼
Nginx  :80          ← serves frontend + proxies /api/* to backend
     │
     ▼
FastAPI  :8000      ← REST API  (/generate, /generate_formatted)
     │
     ▼
LangChain Agent     ← LCEL chain (prompt → LLM → parser)
     │
     ▼
LLM API             ← GitHub Models / OpenAI / Ollama
     │
     ▼
Structured JSON     ← LinkedInPost (Pydantic model)
```

---

## 📂 Project Structure

```
linkedin-post-generator/
├── App/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app & routes
│   ├── linkedin_post_agent.py   # LangChain agent (CLI-usable)
│   └── test_agent.py            # Test suite
├── frontend/
│   └── index.html               # Single-page UI (Tailwind CSS)
├── .env.example                 # Environment variable template
├── .gitignore
├── CONTRIBUTING.md
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── nginx.conf
├── README.md
└── requirements.txt
```

---

## ⚙️ Quick Start

### Option A — Local (no Docker)

**1. Clone & set up environment**
```bash
git clone https://github.com/OmlanHasan007/linkedin-post-generator-ai.git
cd linkedin-post-generator-ai

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Configure your API key**
```bash
cp .env.example .env
```
Edit `.env`:
```env
BASE_URL=https://models.github.ai/inference
API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
```

**3. Run the backend**
```bash
uvicorn App.main:app --reload
```

**4. Open the frontend**

Open `frontend/index.html` in your browser, or visit the API docs at:
```
http://127.0.0.1:8000/docs
```

---

### Option B — Docker (recommended)

**1. Configure environment**
```bash
cp .env.example .env
# Edit .env with your API key
```

**2. Build and start**
```bash
docker compose up --build
```

**3. Open in browser**

| Service  | URL |
|----------|-----|
| Frontend | http://localhost |
| Backend API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

**Useful Docker commands**
```bash
docker compose logs -f          # Stream logs
docker compose down             # Stop services
docker compose up --build -d    # Rebuild + run in background
```

---

## 🌐 API Reference

### `POST /generate`
Returns a structured JSON post.

**Request**
```json
{
  "topic": "AI in Healthcare",
  "language": "English",
  "tone": "Professional"
}
```

**Response**
```json
{
  "title": "Revolutionizing Patient Care with AI",
  "content": "Artificial intelligence is reshaping...",
  "hashtags": ["AIinHealthcare", "DigitalHealth", "MedTech"],
  "call_to_action": "How is your organization leveraging AI? Share below!"
}
```

### `POST /generate_formatted`
Returns a ready-to-paste string instead of JSON.

```json
{
  "formatted_post": "Revolutionizing Patient Care with AI\n\nArtificial intelligence..."
}
```

### `GET /`
Health check — returns `{"status": "ok"}`.

Interactive docs available at `/docs` (Swagger UI) and `/redoc`.

---

## 🧪 Running Tests

```bash
python App/test_agent.py
```

---

## 🔧 Supported LLM Providers

| Provider | BASE_URL | Notes |
|----------|----------|-------|
| GitHub Models | `https://models.github.ai/inference` | Free tier available |
| OpenAI | `https://api.openai.com/v1` | Requires paid key |
| Ollama (local) | `http://localhost:11434` | Fully offline |
| Ollama (Docker) | `http://ollama:11434` | Use with Docker Compose |

---

## 🔐 Security

- `.env` is excluded from git via `.gitignore` — **never commit API keys**
- Use `.env.example` to share configuration templates
- Docker container runs as a non-root user
- Nginx enforces `X-Frame-Options`, `X-Content-Type-Options`, and `X-XSS-Protection` headers

---

## 🚀 Deployment

For production, consider:

1. **HTTPS** — Add SSL certificates to `nginx.conf` (e.g. via Let's Encrypt / Certbot)
2. **Secrets management** — Use Docker secrets or a platform's secret store instead of `.env`
3. **Resource limits** — Add `deploy.resources` constraints in `docker-compose.yml`
4. **Platforms** — Render, Railway, Fly.io, or a VPS all work well with this Docker setup

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Omlan Hasan** — AI & Software Engineering Student  
[GitHub](https://github.com/OmlanHasan007) · [LinkedIn](https://linkedin.com/in/omlan-hasan)
