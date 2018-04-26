from selenium.webdriver.common.by import By


class MainPageLocators(object):
    DISCOVER_SIMTLIX_MENU = (By.XPATH, '//li[@id="nav-menu-item-4491"]/a/span')
    CAREERS_SUBMENU = (By.XPATH, '//li[@id="nav-menu-item-4586"]/a/span/span/span')


class CareersPageLocators(object):
    SEARCH_CATEGORIES = (By.ID, 'search_categories')


class CredentialNetPageLocators(object):
    VERIFY_BUTTON = (By.XPATH, '//*[@id="credential-wrapper"]/div/div[1]/div[2]/div/div/div[2]/div[2]/p/button')
    VERIFIED_LABEL = (By.XPATH, '//*[@id="credential-wrapper"]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/h4/strong')
    TITLE_LABEL = (By.XPATH, '//*[@id="credential-wrapper"]/div/div[2]/div/div/div[2]/h2/a')
