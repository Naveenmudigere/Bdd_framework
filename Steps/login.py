import time

import self as self
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By




@given(u'launch the chrome browser')
def step_impl(self):
    self.driver = webdriver.Chrome("C:/chromedrive/chromedriver.exe")
    self.driver.get("https://www.amazon.in")
    self.driver.implicitly_wait(40)
    self.driver.maximize_window()

    # screenshot
    self.driver.save_screenshot("C:\screenshot\welcome page.jpeg")

    time.sleep(3)




@when(u'search the loptop  and click on lenovo loptop')
def step_impl(self):


    self.driver.find_element(by=By.ID, value="twotabsearchtextbox").send_keys(" lenovo loptops")
    # screenshot
    self.driver.save_screenshot("C:\screenshot\search .jpeg")

    self.driver.find_element(by=By.ID,value="nav-search-submit-button").click()
    # screenshot
    self.driver.save_screenshot("C:\screenshot\submit.jpeg")
@when(u'click on sort by option and select high to low search')
def step_impl(self):

    self.driver.find_element(by=By.XPATH, value='//*[@id="a-autoid-0-announce"]').click()
    time.sleep(5)
    self.driver.find_element(by=By.XPATH, value='//*[@id="s-result-sort-select_2"]').click()




    time.sleep(5)
    self.driver.execute_script("alert(' laptop search successfully');")
    time.sleep(4)

    self.driver.switch_to.alert.dismiss()

    self.driver.refresh()
    time.sleep(8)

@then(u'i will redirect to home page verify the title')
def step_impl(self):

    self.driver.close()
