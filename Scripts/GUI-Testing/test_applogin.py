from playwright.sync_api import Page, BrowserContext, TimeoutError, expect
import pytest 

@pytest.fixture(autouse= True)
def test_login(page: Page):
    page.goto("http://uitestingplayground.com/sampleapp")


def test_successful(page: Page):
    username = "Alles"
    password = "pwd"
    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")

    login_btn = page.get_by_role("button", name= "Log In")

    username_input.fill(username)
    password_input.fill(password)

    login_btn.click()

    label = page.locator("#loginstatus")

    expect(label).to_have_text(f"Welcome, {username}!")

    home_page = page.locator("//a[text()='Home']")
    home_page.click()