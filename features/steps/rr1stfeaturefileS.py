import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)


@given(u'Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(options=options)

@given(u'open Astroyogi Kundaliform page')
def step_impl(context):
    context.driver.get("https://www.astroyogi.com/kundli")
    context.driver.maximize_window()
@given(u'Enter valid details in all the fileds of')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder ='Enter Your Name ']").send_keys("qwertyuiop")
    context.driver.find_element(By.XPATH, "//select[@id ='UserGender']").click()
    context.driver.find_element(By.XPATH, "//option[@value='Female']").click()
    date_dropdown = context.driver.find_element(By.XPATH, "//select[@id = 'Date' ]")
    select = Select(date_dropdown)
    select.select_by_index(7)
    # context.driver.find_element(By.XPATH, "//option[@value='2']/ancestor::select[@id = 'Date']").click()
    month_dropdown = context.driver.find_element(By.XPATH, "//select[@id ='Month']")
    select = Select(month_dropdown)
    select.select_by_index(11)
    year_dropdown = context.driver.find_element(By.XPATH, "//select[@id ='Year']")
    select = Select(year_dropdown)
    select.select_by_visible_text("1987")
    birthTime_hr_ddown = context.driver.find_element(By.XPATH, "//select[@id ='Kund_F_BirthPlace_Hour']")
    select = Select(birthTime_hr_ddown)
    select.select_by_visible_text("10")
    birthTime_min_ddown = context.driver.find_element(By.XPATH, "//select[@id ='Kund_F_BirthPlace_Minute']")
    select = Select(birthTime_min_ddown)
    select.select_by_visible_text("50")
    birthTime_AMPM_ddown = context.driver.find_element(By.XPATH, "//select[@id ='Kund_F_BirthPlace_AM']")
    select = Select(birthTime_AMPM_ddown)
    select.select_by_visible_text("PM")
    search_box = context.driver.find_element(By.ID, "Kund_BirthPlace")
    search_query = "B"
    search_box.send_keys(search_query)
    search_box.send_keys("o")
    search_box.send_keys("k")
    time.sleep(1)
    search_box.send_keys("a")
    wait = WebDriverWait(context.driver, 10)
    suggestions = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id = 'ui-id-1']/li")))

    # Loop through the suggestions and click the one that matches your desired text
    desired_suggestion_text = "Bokaro, Jharkhand, IN"
    for suggestion in suggestions:
        if suggestion.text == desired_suggestion_text:
            suggestion.click()
            break

@when(u'Click on Get Your Kundali button to open kundali resulty page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Get Your Kundli')]").click()
    time.sleep(10)

@then(u'verify that the ResultTable is present on result page')
def verifyResultPage(context):
    resultTable = context.driver.find_element(By.XPATH,
                                              "//table[@class = 'kundli_basic_details' and @id = 'kundlibasicdetailsWebId']").is_displayed()
    assert resultTable is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
