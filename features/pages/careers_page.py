from features.pages.locators import CareersPageLocators


class CareersPage:

    def __init__(self, driver):
        self.driver = driver

    def is_careers_page(self):
        driver = self.driver
        driver.implicitly_wait(10)
        element = driver.find_element(*CareersPageLocators.SEARCH_CATEGORIES)
        return element is not None
