import os
from playwright.sync_api import sync_playwright

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://evozone.wodbuster.com", wait_until="networkidle")

    # Esperar a que cargue completamente
    page.wait_for_timeout(5000)

    # Rellenar login usando placeholders visibles
    page.fill("input[placeholder='email']", USERNAME)
    page.fill("input[type='password']", PASSWORD)

    page.click("button[type='submit']")

    page.wait_for_timeout(5000)

    print("Login realizado correctamente")

    browser.close()


