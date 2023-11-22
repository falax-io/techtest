from playwright.async_api import async_playwright


def before_scenario(context, scenario):
    with async_playwright().start() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/")
        context.page = page
        context.browser = browser


def after_scenario(context, scenario):
    await context.browser.close()
    context.page = {}
    context.browser = {}
