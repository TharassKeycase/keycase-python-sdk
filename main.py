import logging
from keycase_agent.agent import KeycaseAgent
from keycase_agent.config import load_config
from keycase_agent.loader import load_keywords
from typing import Optional, Dict, Any
from dotenv import load_dotenv


def start_agent(config_override: Optional[Dict[str, Any]] = None) -> None:
    """Start the Keycase Agent.

    Args:
        config_override: Optional configuration override dict
    """
    load_keywords()

    if config_override is not None:
        config = config_override
    else:
        config = load_config()

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Log config without sensitive data
    safe_config = {
        k: ('***' if k == 'AGENT_TOKEN' else v)
        for k, v in config.items()
    }
    logger.info("Starting Keycase Agent with configuration: %s", safe_config)

    agent = KeycaseAgent(config)
    agent.start()


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    import os
    if os.getenv('KEYCASE_ENV') == 'development':
        # Development configuration override
        start_agent({
            "HTTP_URL": "http://localhost:3000/api",
            "AGENT_TOKEN": "agt_dev_token_here",
            "AGENT_NAME": "dev-agent-01",
            "AGENT_VERSION": "1.0.0",
            "AGENT_CAPABILITIES": ["selenium", "api"],
            "AGENT_TAGS": ["development", "local"],
        })
    else:
        # Use environment variables from .env
        start_agent()
