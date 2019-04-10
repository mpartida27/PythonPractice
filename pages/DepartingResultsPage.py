from seleniumscripts.BaseTest import Driver
from seleniumscripts.values import CommonResultsPageObjects
from selenium.webdriver.support.ui import Select


class DepartingResultsPage(Driver):

    def select_descendant_drop_down_list(self):
        self.driver.set_page_load_timeout(10)
        self.wait_until_element_is_clickable(CommonResultsPageObjects.ddl_prices)
        select = Select(self.driver.find_element_by_css_selector(CommonResultsPageObjects.ddl_prices))
        select.select_by_value("price:desc")
