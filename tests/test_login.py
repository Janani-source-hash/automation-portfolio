import sys
sys.path.append(".")

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def check_result(actual, expected):
    if actual == expected:
        print("✅ PASS:", actual)
    else:
        print(f"❌ FAIL: Got '{actual}' but expected '{expected}'")

def test_correct_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.enter_username("student")
        login.enter_password("Password123")
        login.click_login()

        actual = login.get_heading()
        check_result(actual, "Logged In Successfully")

        browser.close()

def test_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.enter_username("student")
        login.enter_password("wrongpassword")
        login.click_login()

        actual = login.get_error()
        check_result(actual, "Your password is invalid!")

        browser.close()

def test_wrong_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.enter_username("wronguser")
        login.enter_password("Password123")
        login.click_login()

        actual = login.get_error()
        check_result(actual, "Your username is invalid!")

        browser.close()