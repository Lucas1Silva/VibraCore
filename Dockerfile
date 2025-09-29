# --- Estágio 1: Builder ---
FROM python:3.11-slim as builder

WORKDIR /app

# Instala as ferramentas de build
RUN pip install --upgrade pip build

# Copia o arquivo de dependências
COPY pyproject.toml .

# Cria um ambiente virtual e instala as dependências de produção
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
# O comando "pip install ." lê o pyproject.toml e instala o que está em "dependencies"
RUN pip install .

# --- Estágio 2: Final ---
FROM python:3.11-slim

# O código da aplicação viverá dentro de /app/src
WORKDIR /app/src

# Copia o ambiente virtual com as dependências do estágio "builder"
COPY --from=builder /app/venv /app/venv

# Copia o código da nossa aplicação para a subpasta "src"
COPY ./services/product_service .

RUN useradd --create-home appuser
USER appuser

# Ativa o ambiente virtual para os comandos seguintes
ENV PATH="/app/venv/bin:$PATH"

# Comando para iniciar a aplicação quando o container subir
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]