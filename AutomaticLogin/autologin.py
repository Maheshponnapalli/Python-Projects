from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def startBot(username, password, url):
    # Provide the full path to the chromedriver executable
    chromedriver_path = "C:\\Users\\SINDU\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

    # Set up the service object for ChromeDriver
    service = Service(chromedriver_path)

    # Initialize the webdriver with the service
    driver = webdriver.Chrome(service=service)

    # Open the website
    driver.get(url)

    # Find username input and send the username
    driver.find_element(By.NAME, "login").send_keys(username)

    # Find password input and send the password
    driver.find_element(By.NAME, "password").send_keys(password)

    # Find and click the login button
    driver.find_element(By.NAME, "commit").click()

    print("Login attempted.")
    driver.quit()

# Driver Code
# Replace with your login credentials
username = "Maheshponnapalli"
password = "27may2004@mahi"

# URL of the login page of the site to automate login
url = "https://github.com/login"

# Call the function
startBot(username, password, url)
