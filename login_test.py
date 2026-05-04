def check_login(actual, expected):
    if actual == expected:
        print("✅ PASS:", actual)
    else:
        print(f"❌ FAIL: Got '{actual}' but expected '{expected}'")

print("Running login test suite...")

test_cases = [
    ("Login successful", "Login successful"),
    ("Welcome back!", "Welcome back!"),
    ("Login successful", "Login successful"),
    ("Login failed", "Login successful"),
    ("Error 404", "Welcome back!"),
]

for actual, expected in test_cases:
    check_login(actual, expected)

print("\nTests complete!")