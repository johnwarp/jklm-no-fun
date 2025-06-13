from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Dupe_Scraper():
    def __init__(self, driver):
        self.driver = driver

    def get_dupe(self):
        try:
            input_element = self.driver.find_element(By.CSS_SELECTOR, "div.selfTurn form input.styled")
            value = input_element.get_attribute("value")
        except NoSuchElementException:
            value = None

        return value