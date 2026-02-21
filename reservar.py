import os
from playwright.sync_api import sync_playwright

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # URL de login de WodBuster
    page.goto("https://evozone.wodbuster.com")

    page.fill("input[name='email']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    page.wait_for_timeout(5000)

    print("Login realizado correctamente")

    browser.close()
