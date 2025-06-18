from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/")

    load_delay_link = page.get_by_role("link", name="Load Delay")

    load_delay_link.click()
 
    btn = page.get_by_role("button", name= "Button Appearing After Delay")

    btn.wait_for(timeout=10000)
       
    expect(btn).to_be_visible()

    
    home_page = page.locator("//a[text()='Home']")
    home_page.click()

    title = page.locator("h1#title")
    expect(title).to_contain_text("UI Test Automation")   