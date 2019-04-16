from seleniumscripts.BaseTest import Driver
from seleniumscripts.values import CommonResultsPageObjects
from selenium.webdriver.support.ui import Select


class DepartingResultsPage(Driver):
    name_airline_destination = None

    def select_descendant_drop_down_list(self):
        self.driver.set_page_load_timeout(10)
        self.wait_until_element_is_clickable(CommonResultsPageObjects.ddl_prices)
        select = Select(self.driver.find_element_by_css_selector(CommonResultsPageObjects.ddl_prices))
        select.select_by_value("price:desc")

    def get_prices_and_check_order(self):
        self.wait_for_x_secs(5)
        list_current_prices = self.driver.find_elements_by_xpath(CommonResultsPageObjects.lbl_prices)
        list_current_prices_sortable = [int(i.text.replace("$", "").replace(",", "")) for i in list_current_prices]
        comparable_number = list_current_prices_sortable[0]
        for temp in list_current_prices_sortable:
            assert comparable_number >= temp, "List is not correctly sorted"
            comparable_number = temp

    def click_any_flight(self):
        self.click_any_flight_and_get_names()

