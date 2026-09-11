# Build an AI Agent in Python

A small learning project for building a **tool-using coding agent** in Python.

The agent uses Gemini function calling to inspect files, read file contents, write files, and run Python code inside a bounded working directory. The goal of this project was to learn the mechanics behind agent loops, tool schemas, function dispatch, structured tool responses, and iterative model-tool interaction.

## What this project demonstrates

- Building an agent loop around an LLM
- Defining tool/function schemas
- Dispatching model-selected function calls
- Feeding tool results back into the conversation
- Limiting file/tool operations to a working directory
- Tracking prompt / response token usage in verbose mode
- Testing file-oriented tools independently

## Architecture

```text
User prompt
   ↓
Gemini 2.5 Flash
   ↓
Function call decision
   ↓
Tool dispatcher (`call_function.py`)
   ↓
Filesystem / Python tools
   ↓
Structured tool result
   ↓
Model continues until final response
```

## Available tools

The current dispatcher exposes four functions:

- `get_files_info` — inspect files/directories
- `get_file_content` — read file content
- `write_file` — write content to a file
- `run_python_file` — execute a Python file

For this exercise, tool execution is scoped to the `./calculator` working directory.

## Tech

- Python
- Google Gen AI SDK
- Gemini 2.5 Flash
- `python-dotenv`
- `uv`

## Run locally

Create a `.env` file with a Gemini API key:

```bash
GEMINI_API_KEY=your_key_here
```

Install dependencies, then run:

```bash
python main.py "your prompt"
```

Verbose mode:

```bash
python main.py "your prompt" --verbose
```

## Project structure

```text
.
├── main.py                 # agent loop
├── call_function.py        # tool registry + dispatcher
├── prompts.py              # system instruction
├── functions/              # file / execution tools
├── calculator/             # bounded working directory
└── test_*.py               # tool-level tests
```

## Learning context

This repository is a **learning project**, not a production autonomous coding system. It is useful evidence of how I am building technical fluency around agentic workflows, tool calling, and AI-assisted software development.

For my broader product work, see my Haven portfolio:
https://somber-tamarillo-df3.notion.site/Haven-AI-native-Product-Portfolio-3d8ad9856018811b96ffe8e33a7d48ef
