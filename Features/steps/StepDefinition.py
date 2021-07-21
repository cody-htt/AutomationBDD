from behave import *


@given(u'User open browser, enter URL and navigate to login page')
def step_impl(context):
    context.driver.get(url='http://www.thetestingworld.com/testings')


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@name=\'fld_username\']').send_keys("TungHuynh")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@name=\'fld_password\']').send_keys("123456")
    context.driver.find_element_by_xpath('//input[@name=\'fld_cpassword\']').send_keys("123456")


@when(u'User enters email and address')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@name=\'fld_email\']').send_keys("tunghuynh@gmail.com")
    context.driver.find_element_by_xpath('//input[@name=\'address\']').send_keys("123 ABC")


@when(u'User click on signup button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@value=\'Sign up\']').send_keys("123456")


@then(u'User should register successfully')
def step_impl(context):
    print("Registration is successful")


@when(u'User enters duplicate username')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@name=\'fld_username\']').send_keys("TungHuynhDup")
