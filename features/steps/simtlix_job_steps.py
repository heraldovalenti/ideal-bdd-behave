from behave import given, when, then

from features.pages.careers_page import CareersPage
from features.pages.home_page import HomePage


@given("I am at Simtlix home page")
def simtlix_home_page(context):
    driver = context.driver
    home_page = HomePage(driver)
    context.home_page = home_page
    home_page.open()


@given("Language selected is {language}")
def language_select(context, language):
    home_page = context.home_page
    selected_language = home_page.selected_language()
    assert (selected_language == language), "Expected language is {} but was {}".format(language, selected_language)


@when("I navigate to {menu} menu")
def navigate_menu(context, menu):
    home_page = context.home_page
    navigated_menu = home_page.navigate_menu(menu)
    context.navigated_menu = navigated_menu


@when("I select {submenu} submenu")
def select_submenu(context, submenu):
    home_page = context.home_page
    navigated_menu = context.navigated_menu
    home_page.navigate_submenu(navigated_menu, submenu)


@then("I am presented a list of Open Positions")
def open_positions_page(context):
    driver = context.driver
    careers_page = CareersPage(driver)
    assert careers_page.is_careers_page(), "Expected to be on Careers page"
