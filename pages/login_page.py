class LoginPage:

    def __init__(self, page):
        self.page = page

        # All selectors in one place
        self.username_field = "#username"
        self.password_field = "#password"
        self.submit_button = "#submit"
        self.success_heading = "h1"
        self.error_message = "#error"

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        self.page.fill(self.username_field, username)

    def enter_password(self, password):
        self.page.fill(self.password_field, password)

    def click_login(self):
        self.page.click(self.submit_button)

    def get_heading(self):
        return self.page.inner_text(self.success_heading)

    def get_error(self):
        return self.page.inner_text(self.error_message)