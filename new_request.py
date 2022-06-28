from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


nif = '001030023HO039'

options = Options()
driver = webdriver.Firefox(executable_path='C:/Users/andre.castelo/Downloads/apiaccs_algorithms/browsers_drivers/geckodriver.exe', options=options)
driver.get('https://agt.minfin.gov.ao/PortalAGT/#!/servicos/consultar-nif')

try:
    locate_nif = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'NIF')))
finally:
    locate_nif.send_keys(nif)

try:
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
finally:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='interna']/div[2]/div[2]/div/div/div/div[2]/form/div[3]/button")))
finally:
    locate_consultar = driver.find_element(By.XPATH, "//*[@id='interna']/div[2]/div[2]/div/div/div/div[2]/form/div[3]/button")
    locate_consultar.click()



# locate_nif = driver.find_element(By.ID, 'NIF')
# locate_nif.send_keys(nif)

# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()

# locate_consultar = driver.find_element(By.CLASS_NAME, 'btn ng-binding')
# locate_consultar.click()


# locate_nif = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'NIF')))
# locate_nif.send_keys(nif)


# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()


# # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='interna']/div[2]/div[2]/div/div/div/div[2]/form/div[3]/button"))).click()
# locate_consultar = driver.find_element(By.XPATH, "//*[@id='interna']/div[2]/div[2]/div/div/div/div[2]/form/div[3]/button").click()