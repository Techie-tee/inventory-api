# Contributing

## Before you begin

1. Create and activate a Python virtual environment.
2. Install development dependencies with `pip install -r requirements-dev.txt`.
3. Run `pytest`, `ruff check .`, and `ruff format --check .`.

## Branch names

Use this format:

- `docs/short-description`
- `feat/short-description`
- `fix/short-description`
- `ci/short-description`

## Commit messages

Use this format:

`type: short description`

Examples:

- `docs: add contribution guide`
- `feat: add health endpoint`
- `fix: correct inventory response`

## Pull requests

- Keep each pull request focused on one purpose.
- Explain what changed and how you tested it.
- Do not merge while checks are failing.
- Never commit secrets, tokens, passwords, `.env`, or `.venv` files.