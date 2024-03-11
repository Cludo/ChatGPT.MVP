# ChatGPT.MVP
From ChatGPT to MVP - In-person AI Workshop in Copenhagen

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