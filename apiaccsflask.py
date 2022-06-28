from flask import Flask
from flask import request
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import jsonify


app = Flask(__name__)

@app.route('/',methods=['POST'])
def nifValidator():

    nif = request.form['nif']

    options = Options()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')


    # Instance of Firefox WebDriver is created. 
    # inside container must be /python-docker
    # driver = webdriver.Firefox(executable_path='/python-docker/geckodriver', options=options)
    driver = webdriver.Chrome(executable_path='/python-docker/chromedriver', options=options)


    # The driver.get method will navigate to a page given by the URL: https://sepe.gov.ao/ao/utentes/novo/
    driver.get('https://sepe.gov.ao/ao/utentes/novo/')


    # Locating the elements, filling it and click on the button 'Validar'
    numero_do_contribuinte = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/fieldset/table/tbody/tr[1]/td/div/input")
    numero_do_contribuinte.send_keys(nif)


    # Waiting for nif info show
    wait = WebDriverWait(driver, 10)
    click_validar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmNew"]/fieldset/table/tbody/tr[1]/td/div/a')))
    click_validar.click()


    # Sleep 5 seconds to result
    sleep(10)


    # Locating the element
    nif_info = driver.find_element(By.XPATH, "//*[@id='nif_tipo_nif_info']").text
    nif_text = nif_info


    # Locating and get the element
    name_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/fieldset/table/tbody/tr[2]/td/input")
    name_field_text = name_field.get_attribute('value')


    driver.close()
    driver.quit()

    # return nif_text, name_field_text
    return jsonify(nif_text, name_field_text)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host ='0.0.0.0', port = 5001, debug=True)
