import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configure browser context with a viewport and default timeout.
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720
        },
        "timezone_id": "Europe/London",
        "locale": "en-US"
    }
