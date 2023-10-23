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

driver.get('https://app.digitalinvesting.com.my/user-login')

time.sleep(1)
username = driver.find_elements(By.XPATH,"(//input[@class='form-control ng-untouched ng-pristine ng-invalid'])")[0]
username.send_keys('username/email') #Enter your username/email
password = driver.find_elements(By.XPATH,"(//input[@class='form-control ng-untouched ng-pristine ng-invalid'])")[0]
password.send_keys("password") #Enter your password
LoginButton = driver.find_element(By.CSS_SELECTOR, "button[id='btnNext']").click()

time.sleep(4)
Details = driver.find_elements(By.CSS_SELECTOR, "div[class='box-gradient']")
KDI_Save = driver.find_elements(By.CSS_SELECTOR, "div[class='flex-column flex-md-row d-flex box-orange']")
KDI_Invest = driver.find_elements(By.CSS_SELECTOR, "div[class='flex-column box-orange']")
Total = float(str(''.join((KDI_Save[0].text).split()[2]).replace(',','').split("RM")[1]))+float(str(''.join((KDI_Invest[0].text).split()[5]).replace(',','').split("RM")[1]))

print('Total Value','\n','RM'+str(Total),'\n')
print(''.join([(''.join((Details[0].text).split()[0+i]))+" "  for i in range(2)]))
print(''.join([(''.join((KDI_Save[0].text).split()[0+i]))+" "  for i in range(2)]),''.join((KDI_Save[0].text).split()[3]),''.join([(''.join((KDI_Save[0].text).split()[5+i]))+" "  for i in range(2)]))
print(''.join((KDI_Save[0].text).split()[2]),'   ',''.join((KDI_Save[0].text).split()[4]),'  ',''.join((KDI_Save[0].text).split()[7]),'\n')
print(''.join([(''.join((Details[1].text).split()[0+i]))+" "  for i in range(2)]))
print(''.join([(''.join((KDI_Invest[0].text).split()[3+i]))+" "  for i in range(2)]),''.join((KDI_Invest[0].text).split()[6]),''.join([(''.join((KDI_Invest[0].text).split()[8+i]))+" "  for i in range(2)]))
print(''.join((KDI_Invest[0].text).split()[5]),'   ',''.join((KDI_Invest[0].text).split()[7]),'  ',''.join((KDI_Invest[0].text).split()[10]))

driver.quit()