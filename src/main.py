from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils import Gui, Match_Word, Scraper
import keyboard
import time

def check_room_code(room_code):
    if (len(room_code) != 4):
        return False
    elif not room_code.isalpha():
        return False
    elif room_code != room_code.upper():
        return False
    
    return True

def main():
    ######################################### set up shit
    # initiate driver and get link
    service = Service(executable_path="src/chromedriver.exe")   # ensures we are using the chrome driver that's in the directory
    driver = webdriver.Chrome(service=service)  # launches a new instance of chrome and gives the driver object to control it

    driver.get("https://jklm.fun/DQDZ")
    print("Opening")

    ######################################### update shit

    # do some error checking later so that it's idiot proof
    keyboard.wait("ctrl+alt+t")
    print("hotkey activated")

    driver.switch_to.frame(0)       # switches the context to the iframe with the game logic

    src = driver.page_source
    scraper = Scraper(src)

    result = scraper.get_prompt()

    if result["error"] == None:
        prompt = result["prompt"]
        print(f"The prompt: {prompt}")

        match_word = Match_Word()
        possible_words = match_word.get_word(prompt)

        print("List of possible words:")

        for word in possible_words:
            print(word)

        input("Press enter to exit:")

    else:
        print(result["error"])

    print("Quitting Driver")
    driver.quit()       # we're gonna change this to detach later because we don't want the shit to close on us
    print("driver quitted")

main()
