# Inventory API

A small internal training API used for DevOps apprenticeship work.

## Prerequisites

- Python 3.11 or newer
- Git

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

## Run the API

Start the application:

```powershell
python app.py
```

Open <http://127.0.0.1:8000/inventory> in your browser.

You can also test it in PowerShell:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/inventory
```

## Stopping the Server

In the terminal running the application, press `Ctrl + C`.

## Run tests and code checks

Run these before opening a pull request:

```powershell
pytest
ruff check .
ruff format --check .
```

## Troubleshooting

### PowerShell blocks virtual-environment activation

Run this command in the current PowerShell window, then activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Port 8000 is already in use

Stop the other program using port 8000, or change the port number in `app.py`.

### Python command is not found

Reinstall Python and select **Add Python to PATH**, then open a new PowerShell window.

## Security notes

- The API listens on `127.0.0.1`, meaning it is reachable only from this computer during local development.
- Never commit passwords, API keys, tokens, or `.env` files to GitHub.
- Run `git status` before committing to confirm no secret files will be added.