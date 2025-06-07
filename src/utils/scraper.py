from bs4 import BeautifulSoup

# class='syllable' is our prompt

class Scraper:
    def __init__(self, src):
        self.src = src
        self.soup = BeautifulSoup(src, "html.parser")
    
    def get_prompt(self):
        html = self.soup.find_all(class_="syllable")[0]     # accesses the html element holding the prompt
        prompt = html.get_text()                            # accesses the prompt inside of the html element
        return prompt

    def __str__(self):
        return "crodie"