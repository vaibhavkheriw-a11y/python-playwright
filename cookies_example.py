from playwright.sync_api import sync_playwright
from playwright_config import launch_browser
import json

site = "https://www.w3schools.com"

with sync_playwright() as p:
    browser = launch_browser(p)
    page = browser.new_page()
    page.goto(site)
    cookies = page.context.cookies()
    with open("cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=2)
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    with open("cookies.json", "r", encoding="utf-8") as f:
        cookies = json.load(f)
    context.add_cookies(cookies)
    page.goto(site)
    browser.close()