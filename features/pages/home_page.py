from selenium.webdriver import ActionChains
from locators import MainPageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://www.simtlix.com/"

    def open(self):
        self.driver.get(self.url)

    def selected_language(self):
        current_url = self.driver.current_url
        current_lang = self._retrieve_selected_language(current_url)
        return self._language_string(current_lang)

    def navigate_menu(self, menu):
        driver = self.driver
        menu_selector = self._menu_selector(menu)
        discover_simtlix_menu = driver.find_element(*menu_selector)
        actions = ActionChains(driver)
        actions.move_to_element(discover_simtlix_menu)
        return actions

    def navigate_submenu(self, navigated_menu, submenu):
        driver = self.driver
        submenu_selector = self._submenu_selector(submenu)
        careers_submenu = driver.find_element(*submenu_selector)
        navigated_menu.pause(1)
        navigated_menu.click(careers_submenu)
        navigated_menu.perform()

    def _retrieve_selected_language(self, current_url):
        start_index = len(self.url)
        end_index = start_index + 2
        current_lang = current_url[start_index:end_index]
        return current_lang

    @staticmethod
    def _language_string(language_prefix):
        result = None
        if language_prefix == "en":
            result = "English"
        elif language_prefix == "es":
            result = "Spanish"
        return result

    @staticmethod
    def _menu_selector(menu):
        result = None
        if menu == "Discover Simtlix":
            result = MainPageLocators.DISCOVER_SIMTLIX_MENU
        return result

    @staticmethod
    def _submenu_selector(submenu):
        result = None
        if submenu == "Careers":
            result = MainPageLocators.CAREERS_SUBMENU
        return result
