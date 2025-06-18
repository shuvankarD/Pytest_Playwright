from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/textinput")

    query = "Servus"

    input = page.get_by_label("Set New Button Name")
    input.fill(query)
    btn = page.locator("button.btn-primary")
    btn.click()

    expect(btn).to_have_text(query)



    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   