# AutomaticLogin Project

## Objective
This project automates the login process for websites using Python and Selenium. It allows you to save time and effort by letting the script handle repetitive login tasks.

---

## Prerequisites
Before you begin, ensure you have the following:
1. **Python** installed on your system (version 3.x).
   - Download Python from [python.org](https://www.python.org/downloads/).
2. **Selenium Library**: Selenium is a tool that allows Python to control web browsers.
   - Install it using the command:
     ```bash
     pip install selenium
     ```
3. **WebDriver**: A WebDriver is required to allow Selenium to communicate with your browser. For example, ChromeDriver is used for Google Chrome.

---

## How to Download and Set Up ChromeDriver
1. Find the version of your Google Chrome browser:
   - Open Chrome, go to the menu (`...`) > **Help** > **About Google Chrome**.
   - Note the version number (e.g., `114.0.5735`).
2. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   - Download the driver version that matches your Chrome version.
3. Place ChromeDriver in Your Path:
   - Extract the downloaded file.
   - Move the `chromedriver` executable to a folder in your PATH (e.g., `C:\Windows\System32` on Windows).
   - **OR** place it in your project directory and specify its path in the code.

---

## What is Selenium?
Selenium is a powerful library that allows you to:
- Automate web browser actions like clicking, filling forms, and navigating.
- Perform testing on web applications.
- Automate repetitive browser-based tasks like login.

---

## How to Change the Path of the WebDriver
1. If ChromeDriver is not in your PATH, specify its location in the code:
   ```python
   from selenium import webdriver

   driver = webdriver.Chrome(executable_path="path_to_your_chromedriver")
