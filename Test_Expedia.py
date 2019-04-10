import unittest
from .webdriver import Driver
from .Search_Page import SearchPage


class TestExpedia(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate()

    def test_happy_path_select_flights(self):
        search_page = SearchPage(self.driver)
        search_page.click_flight_button()
        search_page.fill_flight_form()

    def tearDown(self):
        self.driver.close_driver()
