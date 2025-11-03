FROM python:3.13-slim

WORKDIR /bot

RUN pip install uv

COPY pyproject.toml uv.lock* ./
RUN uv sync

COPY tgbot/ ./tgbot/
COPY .env ./

CMD ["uv", "run", "-m", "tgbot"]
