import pytest
from playwright.sync_api import sync_playwright


# Fixture for Playwright instance
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


# Fixture for browser with per-context proxy setting
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


# Fixture for creating a new browser context with a specific proxy
@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()
