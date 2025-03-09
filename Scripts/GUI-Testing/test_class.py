from playwright.sync_api import Page, BrowserContext, expect
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/home")

    class_link = page.locator("//a[text()='Class Attribute']")
    class_link.click()

    primary_button = page.locator("button.btn-primary")
    expect(primary_button).to_be_visible()
    primary_button.click()

    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   