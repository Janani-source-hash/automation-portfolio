# 🤖 Automation Portfolio

![Playwright Tests](https://github.com/Janani-source-hash/automation-portfolio/actions/workflows/tests.yml/badge.svg)

## About
This is my personal test automation portfolio built while transitioning 
from manual testing to automation engineering.

## 🛠️ Tech Stack
- Python 3.14
- Playwright
- Pytest
- GitHub Actions (CI/CD)

## 📁 Project Structure
automation-portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml       ← CI/CD pipeline
├── pages/
│   └── login_page.py       ← Page Object Model
├── tests/
│   └── test_login.py       ← Pytest test cases
└── login_test.py           ← Python basics

## ✅ Test Cases
| Test | Scenario | Status |
|------|----------|--------|
| test_correct_password | Valid login | ✅ Pass |
| test_wrong_password | Invalid password | ✅ Pass |
| test_wrong_username | Invalid username | ✅ Pass |

## 🚀 How to Run
### Install dependencies
pip install playwright pytest
python -m playwright install

### Run tests
pytest tests/test_login.py -v

## 📈 My Journey
- Started with zero coding experience
- Learned Python basics in Phase 1
- Built real browser automation with Playwright
- Implemented Page Object Model
- Set up CI/CD pipeline with GitHub Actions
