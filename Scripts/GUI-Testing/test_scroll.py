from playwright.sync_api import Page, BrowserContext, expect, TimeoutError
import pytest


def test_scroll_page(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role("button", name="Hiding Button")
    btn.wait_for(state="visible")

    btn.scroll_into_view_if_needed()

    page.screenshot(path="test-scroll.jpg")