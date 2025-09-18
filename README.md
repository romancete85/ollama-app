# AI Poem Generator

A Flask web application that generates poems using AI (compatible with Ollama and OpenAI models).

## Features

- Simple web interface for poem generation
- Support for custom AI models via OpenAI-compatible API
- Environment variable configuration

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy the `.env` file and configure your settings
4. Run the server: `python server.py`

## Configuration

The application uses the following environment variables:

- `OPENAI_API_KEY`: Your API key
- `LLM_ENDPOINT`: The endpoint URL for your AI service
- `MODEL`: The model name to use
- `PORT`: Server port (defaults to 3000)

## Files

- `server.py`: Main Flask application
- `requirements.txt`: Python dependencies
- `ollama-app/modelfiles/Modelfile`: Ollama model configuration
- `.env`: Environment variables (not included in repository)