from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    driver = webdriver.Remote(command_executor='http://localhost:9515', desired_capabilities=DesiredCapabilities.CHROME)
    context.driver = driver
    print "Before all"


def after_all(context):
    context.driver.close()
    print "After all"
