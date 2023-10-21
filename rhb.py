from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://onlinebanking.rhbgroup.com/my/login')

username = driver.find_elements(By.NAME, "username")[1]
username.send_keys('account_name') #Enter your account name/ID
LoginButton = driver.find_elements(By.CLASS_NAME, "mdc-button__label")[1].click()

time.sleep(1)
SecureWord = driver.find_elements(By.CSS_SELECTOR, "div[class='eo1y15s0 css-1h01lju-StyledBox e70o5gl0']")[2].click()

password = driver.find_elements(By.NAME, "password")[1]
password.send_keys('password') #Enter your password

time.sleep(1)
LoginButton = driver.find_elements(By.CSS_SELECTOR, "button[class='mdc-button mdc-ripple-upgraded is-rounded css-emnlx8-ButtonBase e1pfhu1r0 mdc-button--unelevated']")[1].click()

time.sleep(2)
try:
    Account = driver.find_elements(By.CSS_SELECTOR, "div[class='css-1id1vi0-StyledBox e70o5gl0']")[0].click()
except:
    time.sleep(2)
    Account = driver.find_elements(By.CSS_SELECTOR, "div[class='css-1id1vi0-StyledBox e70o5gl0']")[0].click()

time.sleep(2)
Money = driver.find_elements(By.CSS_SELECTOR, "div[class='e1d8l7bt0 css-m9mtp2-StyledBox-StyledFlex e70o5gl0']")
print(Money[0].text)                 

driver.quit()

