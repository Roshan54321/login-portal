from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

portal_url = "http://10.100.1.1:8090/httpclient.html"
username = "076bct059"
password = "cax9mx356b"

chrome_driver_path = '/usr/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('ignore-certificate-errors')

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


try:
    eg=driver.get(portal_url)


    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))


    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    driver.quit()

except Exception as e:
    print(e)