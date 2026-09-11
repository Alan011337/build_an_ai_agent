# Build an AI Agent in Python

A small learning project for building a **tool-using coding agent** in Python.

The agent uses Gemini function calling to inspect files, read file contents, write files, and run Python code inside a bounded working directory. The goal of this project was to learn the mechanics behind agent loops, tool schemas, function dispatch, structured tool responses, iterative model-tool interaction, and basic execution boundaries.

## What this project demonstrates

- Building an agent loop around an LLM
- Defining tool/function schemas
- Dispatching model-selected function calls
- Feeding tool results back into the conversation
- Limiting file/tool operations to a working directory
- Tracking prompt / response token usage in verbose mode
- Testing file-oriented tools independently
- Thinking about tool permissions, execution scope, and failure boundaries

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

## Safety / execution boundaries

This project is intentionally bounded rather than designed as a production autonomous coding system.

- File operations are constrained to a working directory.
- The model can only invoke the tools explicitly exposed through the dispatcher.
- Tool calls return structured results back to the model instead of silently mutating arbitrary external systems.
- Python execution is part of the exercise, so the project should be treated as a local learning environment rather than a hardened sandbox.
- There is no claim here of production-grade authorization, isolation, audit logging, rate limiting, or adversarial-security hardening.

These boundaries are part of the learning goal: agent quality depends not only on prompting, but also on **tool design, permissions, execution scope, error handling, and human-visible control points**.

## Product relevance

For AI product work, this project is useful because it makes several product-level questions concrete:

- What actions should an agent be allowed to take?
- Which operations need explicit boundaries or confirmation?
- How should tool results be represented so the model can continue reliably?
- Where can failures occur between model intent, tool dispatch, execution, and the next model step?
- Which capabilities are appropriate for automation versus human review?

The implementation is small, but the underlying concepts map directly to designing safer and more legible agentic product workflows.

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

## Reviewer guide

If you are evaluating this repository for AI PM / TPM technical fluency, the useful questions are:

1. Can I explain the model → function call → dispatcher → tool result → model loop?
2. Can I distinguish tool capability from tool permission?
3. Can I identify where failure, unsafe execution, or ambiguous control could occur?
4. Can I connect those implementation constraints back to product decisions and human oversight?

For product ownership and broader AI-native product evidence, use Haven as the primary source; this repository is supporting implementation evidence.

## Learning context

This repository is a **learning project**, not a production autonomous coding system. It is useful evidence of how I am building technical fluency around agentic workflows, tool calling, bounded execution, and AI-assisted software development.

It does **not** by itself demonstrate production-scale agent reliability, security, observability, or autonomous-software ownership.

For my broader product work, see my Haven portfolio:
https://somber-tamarillo-df3.notion.site/Haven-AI-native-Product-Portfolio-3d8ad9856018811b96ffe8e33a7d48ef
