from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from selenium.webdriver import ActionChains


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/drivers/chromedriver")

    def navigate(self, url="https://www.expedia.com"):
        self.driver.maximize_window()
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string")

    def close_driver(self):
        self.driver.quit()

    def click_element(self, by_element):
        current_by_element = self.driver.find_element_by_css_selector(by_element)
        current_by_element.click()

    def click_element_web_element(self, web_element):
        web_element.click()

    def clear_and_write_on_element(self, css_selector, text_to_write):
        web_element = self.driver.find_element_by_css_selector(css_selector)
        web_element.send_keys(text_to_write)

    def wait_until_element_is_clickable(self, css_selector):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def get_random_number(self, begin, finish):
        return random.randint(begin, finish - 1)

    def move_to_element(self, web_element):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(web_element)

    def move_to_new_window_and_close(self):
        windows_list = self.driver.window_handles
        print(len(windows_list))
        if len(windows_list) > 1:
            print("I am getting executed")
            self.driver.switch_to.window(windows_list[1])
            self.driver.close()
            self.driver.switch_to.window(windows_list[0])

    def move_to_new_window(self):
        windows_list = self.driver.window_handles
        if len(windows_list) > 1:
            self.driver.switch_to.window(windows_list[1])