# 📌 Intelligent Monitoring Platform

### Overview

The **Intelligent Monitoring Platform** is a modular and scalable system designed to continuously monitor services, process operational metrics, and automatically detect anomalous behavior using statistical techniques and machine learning.

This project was developed as a portfolio anchor project, demonstrating backend engineering, data pipelines, anomaly detection, and system architecture in a realistic monitoring scenario.

### Problem Statement

Modern systems generate large volumes of operational data. Detecting abnormal behavior manually is inefficient and error-prone.

This platform addresses that challenge by:

* Continuously collecting metrics from monitored services
* Normalizing heterogeneous data sources
* Detecting anomalies in near real-time
* Generating actionable alerts
* Providing operational visibility through dashboards

### MVP Scope

This MVP focuses on a single, well-defined use case:

**REST API Monitoring**

Monitored metrics:

* Response time (ms)
* HTTP status codes
* Success rate

Data is collected periodically and analyzed using a two-layer anomaly detection strategy.

### Key Features

* Periodic data ingestion from monitored APIs
* Data normalization and validation
* Persistent time-series storage
* Anomaly detection using:
    * Statistical thresholds (rolling mean and Z-score)
    * Machine learning (Isolation Forest)
* Alert generation
* Operational dashboard
* Fully containerized environment (Docker Compose)

### Architecture Overview

The platform follows a pipeline-based architecture:

1. Data ingestion
2. Normalization
3. Storage
4. Anomaly detection
5. Alerting
6. Visualization

### Technology Stack

* **Language:** Python
* **Backend Framework:** FastAPI
* **Database:** PostgreSQL
* **Machine Learning:** Scikit-learn (Isolation Forest)
* **Containerization:** Docker, Docker Compose
* **Visualization:** Lightweight dashboard or Grafana

### Repository Structure
monitoring-platform/
├── app/
│   ├── api/            # FastAPI endpoints
│   ├── ingestion/      # Data collection logic
|   |   ├── collector.py
|   |   ├── scheduler.py
│   ├── normalization/  # Schema validation and transformation
|   |   ├── schemas.py
│   ├── detection/      # Anomaly detection logic
│   ├── alerts/         # Alerting engine
│   ├── storage/        # Database access layer
|   |   ├── database.py
|   |   ├── repository.py
|   |   ├── db_models.py
│   └── main.py
├── ml/
│   ├── training/       # Offline model training
│   ├── models/         # Serialized ML models
│   └── inference/      # Online inference
├── dashboard/
├── simulator/          # API simulator (testing environment)
├── tests/
├── docker-compose.yml
└── README.md

### Anomaly Detection Strategy

The system uses a two-layer detection approach:

1. Statistical Detection

* Rolling mean and standard deviation
* Z-score thresholding

2. Machine Learning Detection

* Isolation Forest trained on historical normal behavior
* Real-time inference on incoming metrics

An alert is triggered when:

* A statistical anomaly is detected, or
* The ML anomaly score exceeds a defined threshold

### Observability Dashboard (Grafana)

The platform includes a Grafana-based dashboard for real-time observability of monitored APIs.

The dashboard provides visibility into:

* Average and P95 response latency per endpoint
* Global response latency trends
* Success rate of API requests
* Automatic anomaly detection events
* Traffic volume over time

Grafana connects directly to the PostgreSQL database using analytical SQL queries, enabling production-grade observability similar to modern SRE platforms.

**Access:**
* URL: http://localhost:3000
* User: admin
* Password: admin


### Running the Project
docker-compose up --build


Once running:

* API: http://localhost:8000
* Dashboard: http://localhost:3000 (if enabled)

### Testing Strategy

* Unit tests for normalization and anomaly detection
* Integration tests for ingestion and persistence
* Controlled anomaly injection using the API simulator

### Future Improvements

* Streaming ingestion (Kafka)
* Autoencoder-based anomaly detection
* Alert integrations (Slack, email)
* Authentication and authorization
* Distributed deployment

### License
MIT License


# 📌 Plataforma Inteligente de Monitoramento

### Visão Geral

A **Plataforma Inteligente de Monitoramento** é um sistema modular e escalável projetado para monitorar continuamente serviços, processar métricas operacionais e detectar automaticamente comportamentos anômalos utilizando técnicas estatísticas e aprendizado de máquina.

Este projeto foi desenvolvido como um projeto âncora de portfólio, demonstrando engenharia de backend, pipelines de dados, detecção de anomalias e arquitetura de sistemas em um cenário realista.

### Problema

Sistemas modernos geram grandes volumes de dados operacionais. A detecção manual de comportamentos anormais é ineficiente e sujeita a erros.

Esta plataforma resolve esse problema ao:

* Coletar métricas continuamente
* Normalizar dados de fontes heterogêneas
* Detectar anomalias quase em tempo real
* Gerar alertas acionáveis
* Fornecer visibilidade operacional por meio de dashboards

### Escopo do MVP

Este MVP foca em um caso de uso único e bem definido:

**Monitoramento de APIs REST**

Métricas monitoradas:

* Tempo de resposta (ms)
* Códigos HTTP
* Taxa de sucesso

Os dados são coletados periodicamente e analisados por uma estratégia de detecção em duas camadas.

### Funcionalidades Principais

* Ingestão periódica de dados
* Normalização e validação
* Armazenamento de séries temporais
* Detecção de anomalias com:
    * Métodos estatísticos
    * Machine Learning (Isolation Forest)
* Geração de alertas
* Dashboard operacional
* Ambiente totalmente containerizado

### Arquitetura

A plataforma segue uma arquitetura orientada a pipeline:

1. Ingestão
2. Normalização
3. Persistência
4. Detecção de anomalias
5. Alertas
6. Visualização

### Stack Tecnológica

* **Linguagem:** Python
* **Backend:** FastAPI
* **Banco de Dados:** PostgreSQL
* **Machine Learning:** Scikit-learn
* **Containerização:** Docker, Docker Compose

### Dashboard de Observabilidade (Grafana)

A plataforma inclui um dashboard baseado em Grafana para observabilidade em tempo real das APIs monitoradas.

O dashboard oferece visibilidade sobre:

* Latência média e P95 por endpoint
* Tendência global de latência
* Taxa de sucesso das requisições
* Eventos de anomalia detectados automaticamente
* Volume de tráfego ao longo do tempo

O Grafana se conecta diretamente ao banco PostgreSQL utilizando consultas SQL analíticas, fornecendo uma experiência próxima a ambientes de produção e práticas de SRE.

**Acesso:**
* URL: http://localhost:3000
* Usuário: admin
* Senha: admin


### Estratégia de Testes

* Testes unitários
* Testes de integração
* Injeção controlada de anomalias via API simulada

### Melhorias Futuras

* Ingestão por streaming
* Autoencoders
* Integrações de alerta
* Autenticação
* Deploy distribuído