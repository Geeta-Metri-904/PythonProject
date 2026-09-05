import pytest
import allure

from playwright.sync_api import Page, expect, sync_playwright

def test_login_page():
    browser = sync_playwright().start().chromium.launch(headless = False)
    Page = browser.new_page()
    Page.goto("https:google.com")
    expect(Page).to_have_title("Google")