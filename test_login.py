from playwright.sync_api import sync_playwright

def check_login(actual, expected):
    if actual == expected:
        print("✅ PASS:", actual)
    else:
        print(f"❌ FAIL: Got '{actual}' but expected '{expected}'")

def test_login_page():
    with sync_playwright() as p:
        # Open browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Store test data — Phase 1 skills! 
        url = "https://practicetestautomation.com/practice-test-login/"
        username = "student"
        password = "Password123"
        expected = "Logged In Successfully"

        # Control the browser — Phase 2 skills!
        print("🌐 Opening browser...")
        page.goto(url)

        print("⌨️ Typing username and password...")
        page.fill("#username", username)
        page.fill("#password", password)

        print("🖱️ Clicking login button...")
        page.click("#submit")

        print("🔍 Checking result...")
        actual = page.inner_text("h1")

        # Phase 1 check_login function!
        check_login(actual, expected)

        browser.close()

# testing wrong password

def test_wrong_password():
    with sync_playwright() as p:
        # Open browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Store test data — Phase 1 skills! 
        url = "https://practicetestautomation.com/practice-test-login/"
        username = "student"
        password = "wrongpassword"
        expected = "Your password is invalid!"

        # Control the browser — Phase 2 skills!
        print("🌐 Opening browser...")
        page.goto(url)

        print("⌨️ Typing username and password...")
        page.fill("#username", username)
        page.fill("#password", password)

        print("🖱️ Clicking login button...")
        page.click("#submit")

        print("🔍 Checking result...")
        actual = page.inner_text("#error")
        check_login(actual, expected)

        browser.close()

print("=" * 40)
print("Running test 1 — correct password")
print("=" * 40)
test_login_page()

print("=" * 40)
print("Running test 2 — wrong password")
print("=" * 40)
test_wrong_password()

print("\n🏆 All tests complete!")