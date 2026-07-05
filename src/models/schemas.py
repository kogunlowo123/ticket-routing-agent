"""Ticket Routing Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class TicketClassification(BaseModel):
    """TicketClassification for Ticket Routing Agent."""
    category: str
    subcategory: str
    affected_service: str
    confidence: float


class RoutingDecision(BaseModel):
    """RoutingDecision for Ticket Routing Agent."""
    ticket_id: str
    assigned_team: str
    assigned_agent: str | None
    reason: str
    sla_hours: int

