from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mode=1000)
    page = browser.new_page()
    page.goto("https://example.com")
    page.wait_for_timeout(10000)
    browser.close()
