import pytest
import re 
from playwright.sync_api import Page, BrowserContext, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_started_page(page: Page):
    
    # page.goto("https://playwright.dev/python")
    page.goto("https://bootswatch.com/default/")
    
    # link = page.get_by_role("link", name="GET STARTED")
    # expect(link).to_be_visible()
    # link.click()
    
    # dropdown = page.locator("ul.dropdown__menu") 
    # expect(dropdown).to_contain_text("Python")

    # docs_link = page.get_by_role("link", name = "Docs")

    # expect(docs_link).to_have_attribute("href", "/python/docs/intro")

    # input = page.get_by_placeholder("Search docs")
    # expect(input).to_be_hidden()

    # search_btn = page.get_by_role("button", name="Search")
    # search_btn.click()
    
    # expect(input).to_be_editable()
    # expect(input).to_be_empty()

    # query = "dashbapu"
    # input.fill(query)

    # expect(input).to_have_value(query)

    default_checkbox = page.get_by_label("Default checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    expect(checked_checkbox).to_be_checked()
    expect(default_checkbox).not_to_be_checked()

    option_menu = page.get_by_label("Example multiple select")
    option_menu.select_option(["1","3"])

    expect(option_menu).to_have_values(["1","3"])

