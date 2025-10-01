# --- Estágio 1: Builder ---
FROM python:3.11-slim as builder
WORKDIR /app
RUN pip install --upgrade pip build
COPY pyproject.toml .
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install .

# --- Estágio 2: Final ---
FROM python:3.11-slim
WORKDIR /app/src
COPY --from=builder /app/venv /app/venv
COPY ./services/review_service .
RUN useradd --create-home appuser
USER appuser
ENV PATH="/app/venv/bin:$PATH"
# O comando é simplesmente rodar o script Python
CMD ["python", "main.py"]