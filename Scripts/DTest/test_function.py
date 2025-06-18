from playwright.sync_api import Page, BrowserContext, expect

def test_doc_links(context: BrowserContext, page: Page):

    page = context.new_page()

    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name = "DOCS")

    expect(docs_link).to_be_visible()

def test_docs_visit(page: Page):
    page.goto("https://playwright.dev/python")

    get_started_link = page.get_by_role("link", name= "GET STARTED")

    get_started_link.click()


