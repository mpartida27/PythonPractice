from SeleniumScripts.values import SearchPageObjects
import time

class SearchPage():

    def __init__(self, driver):
        self.driver = driver

    def click_flight_button(self):
        self.driver.click_element(SearchPageObjects.icon_flight_button)

    def fill_flight_form(self):
        self.driver.clear_and_write_on_element(SearchPageObjects.txt_origin_place,"Mexico City")
        self.driver.wait_until_element_is_clickable(SearchPageObjects.ddl_first_option)
        self.driver.click_element(SearchPageObjects.ddl_first_option)
        self.driver.clear_and_write_on_element(SearchPageObjects.txt_destination_place, "Cancun")
        self.driver.wait_until_element_is_clickable(SearchPageObjects.ddl_first_option)
        self.driver.click_element(SearchPageObjects.ddl_first_option)
        self.driver.clear_and_write_on_element(SearchPageObjects.txt_departing_date,"05/15/2019")
        self.driver.clear_and_write_on_element(SearchPageObjects.txt_returning_date,"06/15/2019")
        self.driver.click_element(SearchPageObjects.btn_search)
