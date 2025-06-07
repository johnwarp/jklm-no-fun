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

def main(room_code):
    # initiate driver and get link
    service = Service(executable_path="src/chromedriver.exe")   # ensures we are using the chrome driver that's in the directory
    driver = webdriver.Chrome(service=service)  # launches a new instance of chrome and gives the driver object to control it

    driver.get("https://jklm.fun/" + room_code)
    print("Opening")

    # do some error checking later so that it's idiot proof
    keyboard.wait("ctrl+alt+t")
    print("hotkey activated")

    driver.switch_to.frame(0)       # switches the context to the iframe with the game logic

    src = driver.page_source
    scraper = Scraper(src)

    prompt = scraper.get_prompt()

    print(prompt)

    input("Press enter to exit:")

    print("Quitting Driver")
    driver.quit()       # we're gonna change this to detach later because we don't want the shit to close on us
    print("driver quitted")

while True:
    room_code = input("Input room code: ")

    if check_room_code(room_code):
        break

main(room_code)
