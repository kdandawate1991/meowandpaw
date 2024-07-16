import pytest
import os
import logging


# fixture to enable logging in report-html
@pytest.fixture(autouse=True)
def capture_logs(caplog):
    caplog.set_level(logging.DEBUG)


# fixture to capture screenshots for ui test failures
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    ui_marker = item.get_closest_marker('ui')

    # Capture and attach screenshot if the test failed
    if report.outcome == 'failed' and ui_marker:
        screenshots_dir = "./screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        pytest_html = item.config.pluginmanager.getplugin('html')
        screenshot_path = os.path.join(screenshots_dir, f"{item.nodeid.replace('::', '_').replace('/', '_')}_failure.png")
        page = item.funcargs["page"]
        page.screenshot(path=screenshot_path)
        extra = getattr(report, "extra", [])
        extra.append(pytest_html.extras.png(screenshot_path))
        report.extra = extra
