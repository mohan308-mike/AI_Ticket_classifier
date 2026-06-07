# Mini AI Ticket Classifier

## Overview

This project uses Llama 3 running locally through Ollama to analyze support tickets and return structured JSON output.

## Requirements

- Python 3
- Ollama
- Llama 3 model

## Installation

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependency:

```bash
pip install ollama
```

Download model:

```bash
ollama pull llama3
```

## Run

```bash
python3 test.py
```

## Validation

The script validates:

- category
- priority
- summary
- recommended_action

Allowed priorities:

- low
- medium
- high
- critical

If the model returns invalid JSON, the script displays an error message.

## Future Improvements

- Better prompt engineering
- More ticket categories
- Save results to a database
- Confidence scores
- Web interface

## Author

Mohan
