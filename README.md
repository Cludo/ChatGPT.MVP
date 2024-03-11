# ChatGPT.MVP
From ChatGPT to MVP - In-person AI Workshop in Copenhagen

## Table of contents

- [Getting started](#getting-started)
  - [Activate virtual environment](#activate-virtual-environment)
  - [Install dependencies](#install-dependencies)
  - [Build](#build)
  - [Run](#run)
- [API](#api)
  - [Start](#start)
  - [Request](#request)
  - [Response (success)](#response-success)
  - [Response (error)](#response-error)
- [Test](#test)

## Getting started

All commands below assume a PowerShell environment on a Windows machine.

### Activate virtual environment

```bash
.\.venv\Scripts\Activate.ps1
```

(deactivate with `deactivate`)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Build

```bash
docker build -t chatgpt-mvp .
```

### Run

```bash
docker run --env OPENAI_API_KEY=$Env:OPENAI_API_KEY -p 8001:8001 chatgpt-mvp
```

## API

### Start

```bash
uvicorn src.main:app --reload --port 8000
```

### Request

```bash
curl -X POST 'http://{hostname}:{port}/v1/chat' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "personality": "string"
}'
```

Parameters:

| Name          | Description           | Type     | Required |
|:--------------|:----------------------|:---------|:---------|
| `personality` | style cue for ChatGPT | `string` | Yes      |

### Response (success)

```json
{
   "error" : null,
   "result" : {
      "answer" : "string"
   }
}
```

### Response (error)

```json
{
   "error" : "string",
   "result" : null
}
```

## Test

Run all tests:

```bash
coverage run -m pytest
```

Get coverage report:

```bash
coverage report
```

Generate html report:

```bash
coverage html
```