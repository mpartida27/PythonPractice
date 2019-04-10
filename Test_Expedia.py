import unittest

from seleniumscripts.pages.DepartingResultsPage import DepartingResultsPage
from .BaseTest import Driver
from seleniumscripts.pages.SearchPage import SearchPage


class TestExpedia(unittest.TestCase):

    def setUp(self):
        self.driver_ = Driver()
        self.driver_.navigate()

    def test_happy_path_select_flights(self):
        search_page = SearchPage()
        search_page.click_flight_button()
        search_page.fill_flight_form()
        results_departing_page = DepartingResultsPage()
        results_departing_page.select_descendant_drop_down_list()

    def tearDown(self):
        self.driver_.close_driver()
