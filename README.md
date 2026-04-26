# 🚀 AI LinkedIn Post Generator

An end-to-end **AI-powered LinkedIn content generator** built using **FastAPI, LangChain, and LLM APIs**.
This application generates **high-quality, structured LinkedIn posts** from a simple topic input, with support for multiple languages and customizable tone.

---

## 📌 Overview

This project demonstrates a **full-stack AI application**:

- 🔹 Backend API (FastAPI)
- 🔹 AI Agent (LangChain + LLM)
- 🔹 Frontend UI (HTML + Tailwind CSS)
- 🔹 Structured Output (Pydantic)

Users can input a topic and instantly generate:

- Title
- Multi-paragraph content
- Hashtags
- Call-to-action

---

## 🧠 Key Features

- ✨ AI-generated professional LinkedIn posts
- 🌍 Multi-language support (English, Spanish, German, etc.)
- 🎯 Structured output (Title, Content, Hashtags, CTA)
- 🎨 Interactive frontend UI
- ⚡ FastAPI backend with REST endpoints
- 🔄 Real-time generation with loading feedback
- 🧩 Modular AI agent design (LangChain-based)

---

## 🏗️ Project Architecture

```text
User Input (Frontend)
        ↓
FastAPI Backend (/generate)
        ↓
LangChain Agent
        ↓
LLM API (GPT model)
        ↓
Structured Response (JSON)
        ↓
Frontend Display
```

---

## 📂 Project Structure

```text
.
├── App/
│   ├── main.py                  # FastAPI backend
│   ├── Lnkedin_post_agent.py   # AI agent logic
│   └── test_agent.py           # Testing script
│
├── frontend/
│   └── index.html              # Frontend UI
│
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── .gitignore
├── env.example
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/OmlanHasan007/linkedin-post-generator-ai.git
cd linkedin-post-generator-ai
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
BASE_URL=https://models.github.ai/inference
API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
```

⚠️ **Important:**

- Never upload `.env` to GitHub
- Use `env.example` for sharing

---

## ▶️ Running the Application

---

### 🔹 Run Backend (FastAPI)

```bash
uvicorn App.main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

### 🔹 Run Frontend

Open:

```text
frontend/index.html
```

---

## 🌐 API Endpoints

### Generate Structured Post

```http
POST /generate
```

Request:

```json
{
  "topic": "AI in Education",
  "language": "English"
}
```

---

### Generate Formatted Post

```http
POST /generate_formatted
```

---

## 📊 Example Output

**Input:**
Topic: _AI in Education_

**Output:**

```text
Revolutionizing Learning: The Power of AI in Education

In today's rapidly evolving world...
...

#AIinEducation #EdTech #FutureOfLearning
```

---

## 🧪 Testing

Run:

```bash
python App/test_agent.py
```

---

## 🐳 Docker Support

Run full stack with Docker:

```bash
docker compose up --build
```

Access:

```
http://localhost:8080
```

---

## 🔐 Security Best Practices

- `.env` is excluded via `.gitignore`
- API keys are never committed
- Use `env.example` for configuration template
- Rotate API keys if exposed

---

## 🧠 My Contribution

- Built and integrated AI agent using LangChain
- Developed FastAPI backend with structured outputs
- Designed frontend UI for interaction
- Implemented full-stack AI workflow
- Secured environment configuration

---

## 🚀 Future Improvements

- 🎨 UI enhancements (modern SaaS design)
- 🧠 Better prompt engineering & tone control
- 🌍 Deployment (Render / Railway / Vercel)
- 📊 Analytics & usage tracking
- 🔐 Authentication system

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Omlan Hasan**
AI & Software Engineering Student

---
