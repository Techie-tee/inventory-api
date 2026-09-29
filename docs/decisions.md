# Technical Decisions

## Local-only server binding

The service listens on 127.0.0.1. This exposes it only on the local computer,
which is appropriate for local development.

## Automated checks

The repository runs tests, linting, and formatting checks in GitHub Actions.
This helps prevent broken or inconsistent code from being merged.

## Secrets

The .env file is ignored by Git. Secrets must never be committed to the
repository.