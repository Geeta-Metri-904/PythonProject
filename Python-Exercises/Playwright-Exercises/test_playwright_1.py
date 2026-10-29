from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    page.screenshot(path="playwright.png")
    browser.close()

from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")