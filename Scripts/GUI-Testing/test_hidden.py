from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")
    green_btn.click()

    with pytest.raises(TimeoutError):
            green_btn.click(timeout=2000)


    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   