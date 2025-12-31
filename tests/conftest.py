"""Pytest configuration and fixtures."""

import pytest
import os
from unittest.mock import Mock, patch


@pytest.fixture
def mock_env_vars():
    """Fixture providing standard environment variables for testing."""
    return {
        'HTTP_URL': 'http://test.localhost:3000/api',
        'AGENT_TOKEN': 'agt_test_token_123456789',
        'AGENT_NAME': 'test-agent-01',
        'AGENT_VERSION': '1.0.0',
        'AGENT_CAPABILITIES': 'selenium,api',
        'AGENT_TAGS': 'test,development'
    }


@pytest.fixture
def mock_config(mock_env_vars):
    """Fixture providing a test configuration dictionary."""
    return {
        'HTTP_URL': mock_env_vars['HTTP_URL'],
        'AGENT_TOKEN': mock_env_vars['AGENT_TOKEN'],
        'AGENT_NAME': mock_env_vars['AGENT_NAME'],
        'AGENT_VERSION': mock_env_vars['AGENT_VERSION'],
        'AGENT_CAPABILITIES': ['selenium', 'api'],
        'AGENT_TAGS': ['test', 'development']
    }


@pytest.fixture
def mock_websocket():
    """Fixture providing a mock WebSocket connection."""
    return Mock()


@pytest.fixture
def mock_auth_credentials():
    """Fixture providing mock authentication credentials."""
    from keycase_agent.auth import AuthCredentials
    from datetime import datetime, timedelta

    return AuthCredentials(
        agent_id=123,
        organization_id=1,
        access_token='test_access_token_123',
        refresh_token='test_refresh_token_456',
        session_id='test_session_id_789',
        ws_url='ws://test.localhost:3000/websocket',
        token_expires_at=datetime.now() + timedelta(hours=24)
    )


@pytest.fixture
def mock_auth_service(mock_auth_credentials):
    """Fixture providing a mock authentication service."""
    mock_service = Mock()
    mock_service.get_token.return_value = 'test_access_token_123'
    mock_service.authenticate.return_value = mock_auth_credentials
    mock_service.get_agent_id.return_value = 123
    mock_service.get_ws_url.return_value = 'ws://test.localhost:3000/websocket'
    mock_service.get_session_id.return_value = 'test_session_id_789'
    mock_service.is_token_valid.return_value = True
    return mock_service


@pytest.fixture
def mock_execution_manager():
    """Fixture providing a mock execution manager."""
    mock_manager = Mock()
    mock_manager.is_running.return_value = False
    mock_manager.start_execution.return_value = None
    mock_manager.stop.return_value = None
    return mock_manager


@pytest.fixture
def mock_state_tracker():
    """Fixture providing a mock state tracker."""
    mock_tracker = Mock()
    mock_tracker.set_busy.return_value = {'busy': False}
    mock_tracker.request_shutdown.return_value = None
    return mock_tracker


@pytest.fixture
def sample_execution_plan():
    """Fixture providing a sample execution plan JSON."""
    return {
        "keywordInstances": [
            {
                "id": 1,
                "keywordName": "test_keyword",
                "name": "Test Keyword Instance",
                "params": [
                    {"name": "param1", "value": "value1"},
                    {"name": "param2", "value": "value2"}
                ]
            }
        ],
        "flows": [
            {
                "id": 1,
                "name": "Test Flow",
                "steps": [
                    {
                        "instanceId": 1,
                        "sequenceOrder": 1
                    }
                ]
            }
        ]
    }


@pytest.fixture
def clean_environment():
    """Fixture that clears environment variables for testing."""
    with patch.dict(os.environ, {}, clear=True):
        yield


@pytest.fixture(autouse=True)
def reset_logging():
    """Fixture to reset logging configuration between tests."""
    import logging
    # Clear any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # Reset logging level
    logging.root.setLevel(logging.WARNING)
    yield
    # Clean up after test
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
