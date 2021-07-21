from selenium.webdriver import Chrome


def before_all(context):
    driver_path = 'F:\\9. Python Selenium RobotFW - Automation Project (Study)\\chromedriver.exe'
    context.driver = Chrome(executable_path=driver_path)


def after_all(context):
    context.driver.close()

# If we have many features in the framework, we should use before_feature/after_feature to control the driver
# This can be use the same with scenarios, steps, tags
#
# def before_feature(context, feature):
#     driver_path = 'F:\\9. Python Selenium RobotFW - Automation Project (Study)\\chromedriver.exe'
#     context.driver = Chrome(executable_path=driver_path)
#
#
# def after_feature(context, feature):
#     context.driver.close()
