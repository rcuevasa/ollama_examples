# Ollama Examples

A collection of Python scripts demonstrating different ways to interact with Ollama API endpoints for text generation and chat functionality.

## Prerequisites

1. **Install Ollama**: Follow the official installation guide at [https://ollama.ai](https://ollama.ai)

2. **Start Ollama server**:
   ```bash
   ollama serve
   ```

3. **Pull required models**:
   ```bash
   ollama pull deepseek-r1:latest
   ollama pull qwen:latest
   ```

## Installation

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Chat Example
Demonstrates the `/api/chat` endpoint with message-based conversation:
```bash
python chat.py
```

### Generate Examples

**Basic generation**:
```bash
python generate.py
```

**Response statistics exploration**:
```bash
python generate_2.py
```
## Scripts Overview

- `chat.py` - Uses the chat endpoint with structured message format
- `generate.py` - Simple text generation using the generate endpoint
- `generate_2.py` - Explores response statistics from the API

## Notes

- All scripts assume Ollama is running on `localhost:11434`
- The server must be running before executing any scripts
- Models can be changed by modifying the `model` field in each script 
