from playwright.sync_api import Page, expect, BrowserContext
import pytest

def test_hover(page: Page):
    page.goto("http://uitestingplayground.com/mouseover")

    link = page.get_by_title("Click me")
    link.hover()

    active_link = page.get_by_title("Active Link")
    active_link.click(click_count=2)

    click_count = page.locator("#clickCount")

    expect(click_count).to_have_text("2")

    home_page = page.locator("//a[text()='Home']")   
    home_page.click()