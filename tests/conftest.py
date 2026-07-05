"""Test configuration for Ticket Routing Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ticket-routing-agent", "category": "IT Operations"}
