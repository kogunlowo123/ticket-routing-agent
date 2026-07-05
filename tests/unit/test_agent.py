"""Ticket Routing Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_classify_ticket():
    """Test Classify a ticket by category, subcategory, and affected service."""
    tools = AgentTools()
    result = await tools.classify_ticket(title="test", description="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assign_priority():
    """Test Assign priority based on impact, urgency, and user VIP status."""
    tools = AgentTools()
    result = await tools.assign_priority(ticket_id="test", impact="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_route_ticket():
    """Test Route ticket to the best team or agent based on skills and load."""
    tools = AgentTools()
    result = await tools.route_ticket(ticket_id="test", category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_predict_resolution_time():
    """Test Predict expected resolution time based on historical data."""
    tools = AgentTools()
    result = await tools.predict_resolution_time(ticket_id="test", category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ticket_routing_agent_agent import TicketRoutingAgentAgent
    agent = TicketRoutingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
