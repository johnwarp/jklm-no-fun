from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import threading
import time

class Dupe_Scraper():
    def __init__(self, driver, word_matcher):
        self.driver = driver
        self.word_matcher = word_matcher

        self.previous_word = ""
        self.current_word = ""
        self.temp_dupes = []

        self.first_gamering = True
        self.element_hidden = False
        self.turn_element = driver.find_element(By.CLASS_NAME, "selfTurn")

    def check_hidden(self):
        die = False
        while not die:
            if not self.turn_element.is_displayed():
                dupe = self.temp_dupes[-1]
                die = True
            time.sleep(0.1)

    def process_word(self):
        print(f"previous word: '{self.previous_word}', current word: '{self.current_word}'")

        if self.previous_word != "" and self.current_word == "":
            if self.first_gamering:
                hidden_check = threading.Thread(target=self.check_hidden, daemon=True)
                hidden_check.start()
                self.first_gamering = False

            self.temp_dupes.append(self.previous_word)
            print(self.temp_dupes)

    def read_word(self):
        try:
            input_element = self.driver.find_element(By.CSS_SELECTOR, "div.selfTurn form input.styled")
            self.previous_word = self.current_word
            self.current_word = input_element.get_attribute("value")
            self.process_word()
        except NoSuchElementException:
            return