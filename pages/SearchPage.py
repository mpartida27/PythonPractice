from seleniumscripts.BaseTest import Driver
from seleniumscripts.values import SearchPageObjects
import time


class SearchPage(Driver):

    def click_flight_button(self):
        self.click_element(SearchPageObjects.icon_flight_button)

    def fill_flight_form(self):
        self.clear_and_write_on_element(SearchPageObjects.txt_origin_place, "Mexico City")
        self.wait_until_element_is_clickable(SearchPageObjects.ddl_first_option)
        self.click_element(SearchPageObjects.ddl_first_option)
        self.clear_and_write_on_element(SearchPageObjects.txt_destination_place, "Cancun")
        self.wait_until_element_is_clickable(SearchPageObjects.ddl_first_option)
        self.click_element(SearchPageObjects.ddl_first_option)
        self.clear_and_write_on_element(SearchPageObjects.txt_departing_date, "05/15/2019")
        self.clear_and_write_on_element(SearchPageObjects.txt_returning_date, "06/15/2019")
        self.click_element(SearchPageObjects.btn_search)
