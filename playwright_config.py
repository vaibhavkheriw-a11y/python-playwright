import os
from dotenv import load_dotenv
load_dotenv()
HEADLESS = os.getenv("HEADLESS", "True").lower() in ("1", "true", "yes")
def launch_browser(playwright):
    return playwright.chromium.launch(headless=HEADLESS)
