import logging
from playwright.sync_api import sync_playwright
from playwright_config import launch_browser

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

with sync_playwright() as p:
    browser = launch_browser(p)
    page = browser.new_page()
    page.on("console", lambda msg: logger.info(f"Console: {msg.text}"))
    page.on("request", lambda request: logger.info(f"Request: {request.url}"))
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjs_console_log")
    page.evaluate("console.log('Playwright logging example')")
    page.wait_for_timeout(1000)
    browser.close()