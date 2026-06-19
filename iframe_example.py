from playwright.sync_api import sync_playwright
from playwright_config import launch_browser

with sync_playwright() as p:
    browser = launch_browser(p)
    page = browser.new_page()
    page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
    frame = page.frame(name="iframeResult")
    if frame:
        content = frame.locator("body").inner_text()
        print(content)
    browser.close()