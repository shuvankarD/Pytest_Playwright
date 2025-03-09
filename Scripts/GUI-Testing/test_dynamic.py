from playwright.sync_api import Page, BrowserContext, expect
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role("button", name="Button with Dynamic ID")
    button.click()

    expect(button).to_be_visible()

    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   
    


