# Backend

## How to start application

Install dependencies

Ensure you have `uv` installed on your system. If not, install it using:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Run app:

uv run uvicorn app.main:app --reload

Create .env

cp .end.sample .env

## Test

pytest