import pytest
import allure

from playwright.sync_api import expect, sync_playwright

def test_login_page():
    #browser page
    browser = sync_playwright().start().chromium.launch(headless = False)
    page = browser.new_page()
    #code interaction with html web page
    page.goto("https:google.com")

#Debugging Purpose
    #breakpoint()

    #validation
    expect(page).to_have_title("Google")
