from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import keyboard
import time

'''
Here's how it's gonna go:
    div with class=selfTurn becomes visible when it's ur turn. Then when it's ur turn, grab the text inside a div with class=syllable.
    (this is ur prompt)

    From there we match it with the words in the word bank and then we type it out probably using selenium or display it to urself
    so you don't look like a dirty ass cheater

Extras & optimizations:
    Using multithreading to search for words faster if it's ass
    Purposefully use big ass words to be scary
    look for words that include the letters you need to gain another life

TODO:
    FIX ALL THIS BULLSHIT
    IFRAMES CAN SUCK MY DING DONG
    ALSO DO THE WAIT BULLSHIT
    wait = WebDriverWait(driver, 10)
    # Wait until the element is present in the DOM
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "syllable")))
    ******THIS SHIT DO THIS
    WHAT'S A NIGGA GOTTA DO TO GET SOME EEL DICK
'''

def grab_prompt(driver):
    time.sleep(1)

    src = driver.page_source

    # print(src)

    soup = BeautifulSoup(src, "html.parser")

    # print("************************")
    # print(soup.markup)
    # print(soup)

    prompt_html = soup.find('div', class_='syllable')

    if prompt_html:
        print("found his ass:", prompt_html)
    else:
        print("didn't find shit")

    return "bruh"

def main():
    service = Service(executable_path="src/chromedriver.exe")
    driver = webdriver.Chrome(service=service)  # launches a new instance of chrome and gives the driver object to control it

    driver.get("https://jklm.fun/VSXT")
    print("Opening")

    keyboard.wait("ctrl+alt+t")
    print("hotkey activated")

    try:
        prompt_text = grab_prompt(driver)
        
    except Exception as e:
        print(f"Soemething went wrong: {e}")
    finally:
        print(f"current url: {driver.current_url}")

    input("Press enter to exit:")

    print("Quitting Driver")
    driver.quit()       # we're gonna change this to detach later because we don't want the shit to close on us
    print("driver quitted")


main()