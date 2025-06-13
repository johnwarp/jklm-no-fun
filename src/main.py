from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import Gui, Match_Word, Scraper, Dupe_Scraper
import tkinter as tk
import keyboard
import threading

# TODO: Check for duplicates effectively

def check_room_code(room_code):
    if (len(room_code) != 4):
        return False
    elif not room_code.isalpha():
        return False
    elif room_code != room_code.upper():
        return False
    
    return True

def scraper_logic(driver, gui, word_matcher):
    first_gaming = True

    while True:
        keyboard.wait("ctrl+alt+t")

        if first_gaming:
            driver.switch_to.frame(0)       # switches the context to the iframe with the game logic
            scraper = Scraper(driver.page_source)
            first_gaming = False

        # scrape the driver's page source for the prompt
        scraper.update_src(driver.page_source)
        result = scraper.get_prompt()

        # checks for errors
        if result["success"]:
            # grabs the prompt and possible words
            prompt = result["data"]
            possible_words = word_matcher.get_word(prompt)
            prompt_dict = {"prompt" : prompt,
                        "words" : possible_words,
                        "error" : False
                        }
        else:
            print(result["error"])
            prompt_dict = {"prompt" : result["data"],
                        "words" : result["error"],
                        "error" : True
                        }
            driver.switch_to.default_content()
            first_gaming = True

        # puts the prompt_dict in the gui's queue and schedules an update
        gui.q.put(prompt_dict)
        gui.schedule_update()

def dupe_logic(driver, word_matcher):
    dupe_scraper = Dupe_Scraper(driver)

    while True:
        # keyboard.wait("enter")
        # print("enter clicked")

        event = keyboard.read_event()

        if event.event_type == "up":
            continue

        duped_word = dupe_scraper.get_dupe()
        print(duped_word)

        if duped_word == None:
            continue
        
        # word_matcher.update_dupes(duped_word)

def main():
    ######################################### set up shit
    # initiate driver and get link
    service = Service(executable_path="src/chromedriver.exe")   # ensures we are using the chrome driver that's in the directory
    driver = webdriver.Chrome(service=service)  # launches a new instance of chrome and gives the driver object to control it

    driver.get("https://jklm.fun/HWTM")
    print("Opening")

    root = tk.Tk()
    gui = Gui(root)

    word_matcher = Match_Word()
    ######################################### update shit

    scraper_thread = threading.Thread(target=scraper_logic, args=(driver, gui, word_matcher), daemon=True)
    get_dupes = threading.Thread(target=dupe_logic, args=(driver, word_matcher), daemon=True)
    scraper_thread.start()
    get_dupes.start()

    root.mainloop()

    print("Quitting Driver")
    driver.quit()       # we're gonna change this to detach later because we don't want the shit to close on us
    print("driver quitted")

main()
