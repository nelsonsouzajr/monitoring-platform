# 📌 API Service Simulator

### Overview

The **API Service Simulator** is a controlled testing service designed to emulate real-world API behavior for monitoring and observability systems.

It allows deterministic simulation of latency, failures, and intermittent behavior, enabling reproducible testing of ingestion pipelines, anomaly detection logic, and alerting mechanisms.

This simulator is a testing and demonstration component, not part of the production monitoring system.

### Purpose

* Provide a stable and configurable API target
* Simulate normal and anomalous behaviors
* Enable deterministic testing of monitoring pipelines
* Support demos and automated tests

### Operating Modes

The simulator operates in predefined modes:

| Mode         |	Description                     |
| normal       |	Low latency, HTTP 200 responses |
| slow         |	Artificial latency injection    |
| error        |	High error rate (HTTP 500)      |
| intermittent |	Random latency and failures     |

The active mode can be changed at runtime.

### Endpoints
| Endpoint     |	Method |	Description                |
| /health      |	GET	   |    Health check               |
| /metrics     |	GET    |    Simulated service response |
| /mode/{mode} |	POST   |    Change simulator mode      |

### Technology Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* **Docker**

### Running Standalone
docker build -t api-simulator .
docker run -p 9000:9000 api-simulator

License

MIT License

# 📌 Simulador de Serviço de API

### Visão Geral

O Simulador de Serviço de API é um serviço de testes controlado, projetado para emular o comportamento de APIs reais em sistemas de monitoramento e observabilidade.

Ele permite a simulação determinística de latência, falhas e comportamento intermitente, possibilitando testes reprodutíveis de pipelines de ingestão, detecção de anomalias e alertas.

Este simulador é um componente de teste e demonstração, não parte do sistema de produção.

### Objetivo

* Fornecer uma API alvo estável e configurável
* Simular comportamentos normais e anômalos
* Permitir testes determinísticos
* Suportar demonstrações e testes automatizados

### Modos de Operação

| Modo         |	Descrição                          |
| normal       |	Baixa latência, respostas HTTP 200 |
| slow         |	Latência artificial                |
| error        |	Alta taxa de erro (HTTP 500)       |
| intermittent |	Latência e falhas aleatórias       |

### Endpoints

| Endpoint     |	Método |	Descrição             |
| /health      |	GET    |	Verificação de saúde  |
| /metrics     |	GET    |	Resposta simulada     |
| /mode/{mode} |	POST   |	Alterar modo          | 

### Stack Tecnológica
* Python
* FastAPI
* Uvicorn
* Docker

### Executando de forma autônoma

docker build -t api-simulator
docker run -p 9000:9000 api-simulator

### License 
MIT License
