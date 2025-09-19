# 🚀 Quick Deployment Guide

## Overview
This guide shows you how to deploy the AI Poem Generator to various platforms.

## 🔧 Prerequisites
- Python 3.8+
- Git
- AI API key (OpenAI or Ollama setup)

## ⚡ Quick Setup

### 1. Clone & Setup
```bash
git clone https://github.com/romancete85/ollama-app.git
cd ollama-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run Locally
```bash
python server.py
# Visit: http://localhost:3000
```

## 🌐 Deployment Options

### Heroku (5 minutes)
```bash
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_key_here
heroku config:set LLM_ENDPOINT=https://api.openai.com/v1
heroku config:set MODEL=gpt-3.5-turbo
git push heroku main
```

### Vercel (3 minutes)
```bash
npm i -g vercel
vercel --prod
# Add environment variables in Vercel dashboard
```

### Railway (10 minutes)
```bash
npm i -g @railway/cli
railway login
railway deploy
# Configure environment variables in Railway dashboard
```

### Traditional Server
```bash
# Install dependencies
sudo apt update && sudo apt install python3 python3-pip nginx

# Setup application
git clone https://github.com/romancete85/ollama-app.git
cd ollama-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Configure environment
cp .env.example .env
# Edit .env with production values

# Run with gunicorn
gunicorn --bind 0.0.0.0:3000 server:app
```

## ⚙️ Environment Variables

### Required Variables
```env
OPENAI_API_KEY=your_openai_key
LLM_ENDPOINT=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
PORT=3000
FLASK_ENV=production
```

### For Ollama (Local)
```env
OPENAI_API_KEY=ollama
LLM_ENDPOINT=http://localhost:11434/v1
MODEL=llama3.2
PORT=3000
FLASK_ENV=production
```

## 🔍 Troubleshooting

### Common Issues
- **Port already in use**: Change PORT in .env
- **API key errors**: Verify your OpenAI API key
- **Import errors**: Ensure virtual environment is activated
- **Permission errors**: Check file permissions on server

### Health Check
```bash
curl http://localhost:3000/
# Should return the HTML interface
```

---

**Repository**: https://github.com/romancete85/ollama-app  
**Status**: ✅ Ready to Deploy
