
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://google.com.br")
    page.wait_for_timeout(5000)
    page.screenshot(path="example.png") # Comando que printa a tela
    browser.close()