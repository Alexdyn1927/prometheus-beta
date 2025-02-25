import pytest
import logging

@pytest.fixture(autouse=True)
def setup_logging():
    """Configure logging for tests."""
    logging.basicConfig(level=logging.INFO)

pytest.register_assert_rewrite('tests.test_network_logger')