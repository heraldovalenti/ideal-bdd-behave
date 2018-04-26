from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.locators import CredentialNetPageLocators


class CredentialNetPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.credential.net/"

    def navigate_certificate_key(self, certificate_key):
        path = self.url + certificate_key
        self.driver.get(path)

    def select_option(self, option):
        driver = self.driver
        driver.implicitly_wait(10)
        option_selector = self._option_selector(option)
        option_element = driver.find_element(*option_selector)
        option_element.click()

    def is_certificate_verified(self):
        certificate_verified = False
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected_condition = EC.element_to_be_clickable(CredentialNetPageLocators.VERIFIED_LABEL)
        verified_label = wait.until(expected_condition)
        if verified_label is not None:
            certificate_verified = verified_label.is_displayed()
        return certificate_verified

    def certificate_title(self):
        title_value = None
        driver = self.driver
        title_label = driver.find_element(*CredentialNetPageLocators.TITLE_LABEL)
        if title_label is not None:
            title_value = title_label.text
        return title_value

    @staticmethod
    def _option_selector(option):
        result = None
        if option == "Verify":
            result = CredentialNetPageLocators.VERIFY_BUTTON
        return result
