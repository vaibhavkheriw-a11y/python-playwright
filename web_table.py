from playwright.sync_api import sync_playwright
from playwright_config import launch_browser
with sync_playwright() as p:
    browser = launch_browser(p)
    page = browser.new_page()
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    rows = page.locator("#customers tr")
    for i in range(1, rows.count()):
        row = rows.nth(i)
        cells = row.locator("td")
        values = [cells.nth(j).inner_text().strip() for j in range(cells.count())]
        print(values)
    browser.close()
