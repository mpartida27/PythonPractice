from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from selenium.webdriver import ActionChains


def click_element_css_selector(css_selector):
    web_element = driver.find_element_by_css_selector(css_selector)
    web_element.click()


def click_element_web_element(web_element):
    web_element.click()

def clear_and_write_on_element(css_selector, text_to_write):
    web_element = driver.find_element_by_css_selector(css_selector)
    web_element.send_keys(text_to_write)


def wait_until_element_is_clickable(css_selector):
    wait = WebDriverWait(driver, 20)
    # que pedo con esto 0.0 (le estoy enviando una tupla?)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))


def get_random_number(begin, finish):
    return random.randint(begin, finish-1)


def move_to_element(web_element):
    action_chains = ActionChains(driver)
    action_chains.move_to_element(web_element)


if __name__ == "__main__":
    try:
        # this has to be in a method
        driver = webdriver.Chrome("/Users/drivers/chromedriver")
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get("https://www.expedia.com")

        # click on flights button
        click_element_css_selector("#tab-flight-tab-hp")

        # write on origin text field and Select the first option
        clear_and_write_on_element("#flight-origin-hp-flight", "Mexico City")
        wait_until_element_is_clickable("#aria-option-0")
        click_element_css_selector("#aria-option-0")

        # write on destination text field
        clear_and_write_on_element("#flight-destination-hp-flight", "Cancun")
        wait_until_element_is_clickable("#aria-option-0")
        click_element_css_selector("#aria-option-0")

        # select departing date
        clear_and_write_on_element("#flight-departing-hp-flight", "05/15/2019")

        # select returning date
        clear_and_write_on_element("#flight-returning-hp-flight", "06/15/2019")

        # click on submit button
        click_element_css_selector("#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button")

        '''Origin Page'''
        driver.set_page_load_timeout(10)
        wait_until_element_is_clickable("#sortDropdown")
        select = Select(driver.find_element_by_css_selector("#sortDropdown"))
        select.select_by_value("price:desc")

        # hardcode time sleep TODO search how to execute JavaScript or if python has already a method
        time.sleep(4)

        # create prices list
        list_current_prices = driver.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")
        # list_current_prices_sortable = ["".join(list(filter(lambda x: x != '$' and x != ',', i.text))) for i in list_current_prices]
        list_current_prices_sortable = [int(i.text.replace("$", "").replace(",", "")) for i in list_current_prices]

        comparable_number = list_current_prices_sortable[0]
        # check if the list is correctly sorted
        for i in list_current_prices_sortable:
            assert comparable_number >= i, "The list is not sorted correctly"
            comparable_number = i

        # create a list of Select button
        list_current_select_button = driver.find_elements_by_xpath("//button[contains(@class,'t-select-btn')]")
        random_number = get_random_number(0,len(list_current_select_button))
        print(random_number)
        move_to_element(list_current_select_button[random_number])
        click_element_web_element(list_current_select_button[random_number])

        # this has to be in a method

    finally:
        driver.quit()

