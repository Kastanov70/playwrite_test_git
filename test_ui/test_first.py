import os

import pytest
from playwright.async_api import Playwright


@pytest.mark.smoke
def test_for_start(playwright: Playwright):
    browser = playwright.chromium.launch()
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://skillotron.com/")
    # Go to https://skillotron.com/signin
    page.goto("https://skillotron.com/signin")
    # Click text=News
    page.click("text=News")
    assert page.url == "https://skillotron.com/news"
    # Click h1:has-text("News")
    assert page.text_content("h1:has-text(\"News\")") == os.environ["NAME"]
