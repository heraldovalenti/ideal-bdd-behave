import unittest

from features.pages.home_page import HomePage


class HomePageTests(unittest.TestCase):

    def test_retrieve_selected_language(self):
        current_url = "http://www.simtlix.com/en/home/"
        home_page = HomePage(None)
        lang_prefix = home_page._retrieve_selected_language(current_url)
        self.assertEquals("en", lang_prefix)

    def test_language_string_english(self):
        home_page = HomePage(None)
        lang = home_page._language_string("en")
        self.assertEquals("English", lang)

    def test_language_string_spanish(self):
        home_page = HomePage(None)
        lang = home_page._language_string("es")
        self.assertEquals("Spanish", lang)


if __name__ == '__main__':
    unittest.main()
