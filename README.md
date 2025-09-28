# VibraCore 🚀

![CI Pipeline](https://github.com/<SEU-USUARIO>/VibraCore/actions/workflows/ci.yml/badge.svg)

## 🎯 Sobre o Projeto

**VibraCore** é um projeto de estudo e demonstração para construir uma arquitetura de microsserviços moderna, resiliente e escalável. O objetivo é explorar as melhores práticas de desenvolvimento, DevOps e infraestrutura como código (IaC).

Começamos com uma base sólida de automação (CI/CD) e qualidade de código, para depois evoluir para containers (Docker), comunicação assíncrona (Kafka) e orquestração na nuvem com Terraform.

## 🛠️ Tech Stack (Planejado)

- **Linguagem:** Python 3.10+
- **Framework API:** FastAPI (planejado)
- **Containerização:** Docker
- **Comunicação Assíncrona:** Apache Kafka
- **API Gateway:** Kong / AWS API Gateway (a definir)
- **Infraestrutura como Código (IaC):** Terraform
- **CI/CD:** GitHub Actions
- **Provedor de Nuvem:** AWS / GCP (a definir)

## 🏁 Fase Atual: Fase 1 - A Fundação

Atualmente, o projeto está na sua fase inicial, com foco em estabelecer uma base de desenvolvimento profissional:

- [x] Estrutura do projeto definida.
- [x] Esteira de Integração Contínua (CI) com GitHub Actions.
- [x] Linting (`flake8`) e formatação (`black`) automatizados.
- [x] Hooks de Git (`pre-commit`) para garantir a qualidade do código localmente.
- [x] Configuração de testes com `pytest`.

## 🚀 Como Começar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)<SEU-USUARIO>/VibraCore.git
    cd VibraCore
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .[dev]
    ```

3.  **Configure os Git Hooks:**
    ```bash
    pre-commit install
    ```

4.  **Rode os testes para verificar se tudo está funcionando:**
    ```bash
    pytest
    ```

## 📜 Próximos Passos

Consulte o plano de desenvolvimento nas issues do projeto (a criar). O próximo grande passo é a **Fase 2: Containerização com Docker**.

---
*Lembre-se de substituir `<SEU-USUARIO>` pelo seu nome de usuário do GitHub.*
