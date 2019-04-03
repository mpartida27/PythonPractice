from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

currentElement = (By.CSS_SELECTOR,"#tab-flight-tab-hp")


def click_element(css_selector):
    web_element = driver.find_element_by_css_selector(css_selector)
    web_element.click()


def clear_and_write_on_element(css_selector, text_to_write):
    web_element = driver.find_element_by_css_selector(css_selector)
    web_element.send_keys(text_to_write)


def wait_until_element_is_clickable(css_selector):
    wait = WebDriverWait(driver, 20)
    #que pedo con esto 0.0 (le estoy enviando una tupla?)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector)))


if __name__ == "__main__":
    # this has to be in a method
    driver = webdriver.Chrome("/Users/drivers/chromedriver")
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get("https://www.expedia.com")

    # click on flights button
    click_element("#tab-flight-tab-hp")

    # write on origin text field and Select the first option
    clear_and_write_on_element("#flight-origin-hp-flight", "Mexico City")
    wait_until_element_is_clickable("#aria-option-0")
    click_element("#aria-option-0")

    # write on destination text field
    clear_and_write_on_element("#flight-destination-hp-flight", "Cancun")
    wait_until_element_is_clickable("#aria-option-0")
    click_element("#aria-option-0")

    # this has to  be in a method
    driver.quit()
