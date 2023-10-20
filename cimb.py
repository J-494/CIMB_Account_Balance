from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument('--no-sandbox')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.cimbclicks.com.my/clicks')

username = driver.find_element(By.NAME, "username") 
username.send_keys('account_name') #Enter your account name/ID
username.send_keys(Keys.RETURN)

time.sleep(2)
Secureword = driver.find_element(By.XPATH,"//label[text()='Yes, this is my SecureWord']")
try:
    Secureword.click()
except:
    print("Please try again ten minites later")
    exit()

password = driver.find_element(By.NAME, "password")  
password.send_keys('password') #Enter your password
password.send_keys(Keys.RETURN)

time.sleep(3)
Money = driver.find_element(By.XPATH,"(//div[@id='dashboardhome_accordian_header0'])")
print(''.join([(''.join((Money.text).split()[10+i]))+" "  for i in range(8)]),'\n',''.join((Money.text).split()[3]),''.join((Money.text).split()[4]),"\n",''.join((Money.text).split()[5]),''.join((Money.text).split()[6]))
                   
driver.quit()

