# 📊 Grafana Dashboards – Intelligent Monitoring Platform

## Overview

This directory contains the official Grafana dashboards used by the **Intelligent Monitoring Platform**.

Dashboards are versioned as JSON files and automatically provisioned via Docker to ensure reproducibility, portability, and infrastructure-as-code best practices.

The dashboards provide real-time and historical visibility into API performance, reliability, and anomaly detection.

---

## Dashboards Included

### Monitoring Platform Dashboard

Key metrics visualized:

#### Performance
- Average latency per endpoint (time series)
- P95 latency per endpoint (time series)

#### Executive Overview
- Global success rate (%)
- Global average latency (ms)
- P95 latency summary

#### Intelligence
- Anomaly occurrences over time
- Anomaly table for inspection

---

## Metrics Definitions

- **Average Latency**  
  Mean response time over the selected period.

- **P95 Latency**  
  95th percentile response time, highlighting tail latency.

- **Success Rate**  
  Percentage of requests with successful responses (HTTP < 500).

- **Anomalies**  
  Events flagged by the anomaly detection engine.

---

## Provisioning

Dashboards are automatically provisioned at Grafana startup using:

- Dashboard provisioning files
- PostgreSQL datasource provisioning

No manual dashboard import is required.

---

## Access

- Grafana UI: http://localhost:3000  
- Default credentials:
  - User: `admin`
  - Password: `admin`

---

## Versioning Strategy

- Dashboards are exported as JSON
- Changes must be committed to version control
- JSON files should not be edited manually unless necessary

---

## Notes

These dashboards are designed for **portfolio demonstration**, emphasizing observability concepts, SRE metrics, and anomaly-driven monitoring.

# 📊 Dashboards Grafana – Plataforma Inteligente de Monitoramento

## Visão Geral

Este diretório contém os dashboards oficiais do Grafana utilizados pela **Plataforma Inteligente de Monitoramento**.

Os dashboards são versionados em arquivos JSON e provisionados automaticamente via Docker, seguindo práticas de infraestrutura como código.

Os painéis fornecem visibilidade em tempo real e histórica sobre desempenho, confiabilidade e anomalias da API monitorada.

---

## Dashboards Disponíveis

### Dashboard Monitoring Platform

Métricas principais:

#### Performance
- Latência média por endpoint
- Latência P95 por endpoint

#### Visão Executiva
- Taxa de sucesso global (%)
- Latência média global (ms)
- Resumo de latência P95

#### Inteligência
- Ocorrências de anomalias ao longo do tempo
- Tabela de eventos anômalos

---

## Definição das Métricas

- **Latência Média**  
  Tempo médio de resposta no período selecionado.

- **Latência P95**  
  Percentil 95, destacando latências de cauda.

- **Taxa de Sucesso**  
  Percentual de requisições bem-sucedidas (HTTP < 500).

- **Anomalias**  
  Eventos detectados pelo mecanismo de detecção.

---

## Provisionamento

Os dashboards são carregados automaticamente na inicialização do Grafana usando arquivos de provisionamento.

Nenhuma importação manual é necessária.

---

## Acesso

- Grafana: http://localhost:3000  
- Credenciais padrão:
  - Usuário: `admin`
  - Senha: `admin`

---

## Estratégia de Versionamento

- Dashboards exportados em JSON
- Alterações devem ser commitadas
- Evitar edição manual fora do Grafana

---

## Observação

Estes dashboards foram projetados para fins de portfólio, destacando conceitos de observabilidade, métricas SRE e monitoramento inteligente.
