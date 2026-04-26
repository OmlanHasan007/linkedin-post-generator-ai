# Contributing to AI LinkedIn Post Generator

Thank you for your interest in contributing! This guide will help you get started.

---

## 🐛 Reporting Bugs

1. Search [existing issues](../../issues) first — it may already be reported.
2. Open a new issue using the **Bug Report** template.
3. Include: OS, Python version, steps to reproduce, expected vs. actual behaviour.

---

## 💡 Suggesting Features

1. Open an issue using the **Feature Request** template.
2. Describe the problem you're solving and your proposed solution.
3. Wait for maintainer feedback before starting work.

---

## 🛠️ Development Setup

```bash
# 1. Fork & clone
git clone https://github.com/YOUR_USERNAME/linkedin-post-generator-ai.git
cd linkedin-post-generator-ai

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API key

# 5. Run the backend
uvicorn App.main:app --reload

# 6. Open the frontend
# Open frontend/index.html in your browser
```

---

## 📋 Pull Request Checklist

- [ ] Branch off `main`: `git checkout -b feat/my-feature`
- [ ] Follow the existing code style (clear names, type hints, docstrings)
- [ ] Test your changes: `python App/test_agent.py`
- [ ] Update `README.md` if you changed behaviour or added features
- [ ] Write a clear PR description: what, why, how

---

## 📐 Code Style

- **Python**: Follow [PEP 8](https://pep8.org/). Use type hints.
- **Commits**: Use conventional commits — `feat:`, `fix:`, `docs:`, `refactor:`
- **Docstrings**: Google style for all public functions and classes.

---

## 🔐 Security

Never commit API keys or `.env` files. If you accidentally expose a key, revoke it immediately and rotate it.

---

Thank you for contributing! 🎉
