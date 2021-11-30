import pytest
from playwright.async_api import Playwright


@pytest.mark.smoke
def test_for_start(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.click("[aria-label=\"Найти\"]")
    page.fill("[aria-label=\"Найти\"]", "playwright")
    with page.expect_navigation():
        page.press("[aria-label=\"Найти\"]", "Enter")
    page.click("text=https://playwright.dev")
    # assert page.url == "https://playwright.dev/"
