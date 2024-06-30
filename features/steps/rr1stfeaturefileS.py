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
    context.driver.get("https://www.astroyogi.com/kundli")
    context.driver.maximize_window()
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


    # Wait for the suggestions to appear
    wait = WebDriverWait(context.driver, 10)
    suggestions = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id = 'ui-id-1']/li")))

    # Loop through the suggestions and click the one that matches your desired text
    desired_suggestion_text = "Bokaro, Jharkhand, IN"
    for suggestion in suggestions:
        if suggestion.text == desired_suggestion_text:
            suggestion.click()
            break

    # Close the WebDriver
    # context.driver.quit()
    # ActionChains(context.driver)\
    #     .send_keys_to_element(text_input, "b")\
    #     .perform()
    # # birthPlace_Ddown.click()
    # birthPlace_Ddown.clear()
    # birthPlace_Ddown.send_keys("bokaro")
    # birthPlace_Ddown.send_keys("bokaro").send_keys(Keys.ARROW_DOWN)
    # birthPlace_Ddown.send_keys(Keys.ARROW_DOWN)
    # # elements = WebDriverWait(context.driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "ui-id-10")))
    # # context.driver.find_element(By.XPATH, "//span[@class ='sprite-kundli-page LightYellowIcon sprite-heading-kundli']").click()
    # birthPlace_Ddown.send_keys(Keys.)
    # birthPlace_Ddown.send_keys(Keys.NUMPAD4)
    time.sleep(5000)
    # print(elements)
    # actions = ActionChains(context.driver)
    # actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
    # Value_ddown = context.driver.find_element(By.XPATH, "//input[@id = 'Kund_BirthPlace']").get_attribute()
    # context.driver.find_element(By.ID, "ui-id-10").click()
    # items = html_list.find_elements_by_tag_name("li")
    # for item in items:
    #     text = item.
    #     print(text)
    # time.sleep(2000)
    # context.driver.find_element(By.XPATH, "//div[@tabindex = -1 and @class='ui-menu-item-wrapper']").click()
    # context.driver.find_element(By.XPATH, "//button[@id = 'kundli_submit']").click()
    # time.sleep(10)

@when(u'Astroyogi KundaliResult page is open')
def KundaliResult(context):
    resultTable = context.driver.find_element(By.XPATH,
                                              "//table[@class = 'kundli_basic_details' and @id = 'kundlibasicdetailsWebId']")


@then(u'verify that the ResultTable is present on result page')
def verifyResultTable(context):
    raise NotImplementedError(u'STEP: Then verify that the Logo present on homepage')


@then(u'close browser')
def closeBrowser(context):
    raise NotImplementedError(u'STEP: Then close browser')
