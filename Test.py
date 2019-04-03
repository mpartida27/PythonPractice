from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome("/Users/drivers/chromedriver")

    def set_up_test_case(self):
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.driver.get("https://www.expedia.com")
        self.driver.quit()

    def finish_test_case(self):
        self.driver.quit()

if __name__ == "__main__":
    baseTest = BaseTest()
    baseTest.set_up_test_case()

    baseTest.finish_test_case()
