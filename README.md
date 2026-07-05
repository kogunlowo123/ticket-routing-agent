# Ticket Routing Agent

[![CI](https://github.com/kogunlowo123/ticket-routing-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ticket-routing-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Intelligent ticket routing agent that classifies incoming IT tickets, assigns priority and category, routes to the appropriate support team, predicts resolution time, and balances workload across agents.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `classify_ticket` | Classify a ticket by category, subcategory, and affected service |
| `assign_priority` | Assign priority based on impact, urgency, and user VIP status |
| `route_ticket` | Route ticket to the best team or agent based on skills and load |
| `predict_resolution_time` | Predict expected resolution time based on historical data |
| `rebalance_queue` | Rebalance ticket queues across agents for optimal throughput |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/routing/classify` | Classify ticket |
| `POST` | `/api/v1/routing/prioritize` | Assign priority |
| `POST` | `/api/v1/routing/route` | Route ticket |
| `POST` | `/api/v1/routing/predict-resolution` | Predict resolution time |
| `POST` | `/api/v1/routing/rebalance` | Rebalance queues |

## Features

- Ticket Classification
- Priority Assignment
- Team Routing
- Resolution Prediction
- Workload Balancing

## Integrations

- Servicenow
- Jira Service Management
- Freshservice
- Zendesk
- Pagerduty

## Architecture

```
ticket-routing-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ticket_routing_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ITSM Platform + ML Classification + Queue Management**

---

Built as part of the Enterprise AI Agent Platform.
