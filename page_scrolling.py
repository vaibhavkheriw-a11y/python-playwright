from playwright.sync_api import sync_playwright
from playwright_config import launch_browser

with sync_playwright() as p:
    browser = launch_browser(p)
    page = browser.new_page()
    page.goto("https://www.w3schools.com/howto/howto_css_sticky_element.asp")
    page.evaluate("window.scrollBy(0, 800)")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    browser.close()
