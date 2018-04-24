from selenium.webdriver.common.by import By


class MainPageLocators(object):
    DISCOVER_SIMTLIX_MENU = (By.XPATH, '//li[@id="nav-menu-item-4491"]/a/span')
    CAREERS_SUBMENU = (By.XPATH, '//li[@id="nav-menu-item-4586"]/a/span/span/span')


class CareersPageLocators(object):
    SEARCH_CATEGORIES = (By.ID, 'search_categories')
