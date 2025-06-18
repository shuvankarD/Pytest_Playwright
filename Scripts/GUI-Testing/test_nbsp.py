from playwright.sync_api import Page, expect, BrowserContext, TimeoutError
import pytest

def test_hover(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")

    page.locator("//button[starts-with(text(), 'My')]").click(timeout=2000)

    

    home_page = page.locator("//a[text()='Home']")   
    home_page.click()