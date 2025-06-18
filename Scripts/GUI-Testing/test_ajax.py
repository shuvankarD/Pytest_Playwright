from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/")

    ajax = page.locator("button#ajaxButton")
    ajax.click()

    para = page.locator("p.Data loaded with AJAX get request.")

    para.wait_for()

    expect(para).to_be_visible()

    expect()
    
    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   