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

    def execute_dupes(self):
        dupe = self.temp_dupes[-1]
        self.word_matcher.update_dupes(dupe)
        self.temp_dupes = []

    def check_hidden(self):
        print("thread created")
        turn_element = self.driver.find_element(By.CLASS_NAME, "selfTurn")
        die = False
        while not die:
            if not turn_element.is_displayed():
                self.execute_dupes()
                die = True
            time.sleep(0.1)
        self.first_gamering = True
        print(self.word_matcher.dupes)
        print("thread destroyed")

    def process_word(self, new_word):
        self.previous_word = self.current_word
        self.current_word = new_word

        if self.previous_word != "" and self.current_word == "":
            # only runs the first time process_word has been called
            if self.first_gamering:
                hidden_check = threading.Thread(target=self.check_hidden, daemon=True)
                hidden_check.start()
                self.first_gamering = False

            self.temp_dupes.append(self.previous_word)

    def read_word(self):
        try:
            input_element = self.driver.find_element(By.CSS_SELECTOR, "div.selfTurn form input.styled")
            self.process_word(input_element.get_attribute("value"))
        except NoSuchElementException:
            return