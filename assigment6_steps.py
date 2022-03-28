from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given('I am on the python.org homepage')
def step(context):
    context.driver = webdriver.Chrome('./chromedriver')
    context.driver.get("http://www.python.org")

@when('I enter the search "{search}"')
def step_impl(context, search):
   elem = context.driver.find_element_by_name("q")
   elem.send_keys(search)
   elem.send_keys(Keys.RETURN)

@then('Search results are displayed')
def step_impl(context):
    if ("No results found." in context.driver.page_source):
        raise Exception ("No results were found")