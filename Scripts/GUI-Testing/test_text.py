from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest


def test_scroll_page(page: Page):
    page.goto("http://uitestingplayground.com/verifytext")

    text = page.locator("div.bg-primary").get_by_text("Welcome", exact= False)


    expect(text).to_have_text("Welcome UserName!")

