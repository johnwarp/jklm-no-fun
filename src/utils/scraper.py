from bs4 import BeautifulSoup

# class='syllable' is our prompt

class Scraper:
    def __init__(self, src):
        self.src = src
        self.soup = BeautifulSoup(src, "html.parser")
    
    def get_prompt(self):
        try:
            html = self.soup.find_all(class_="syllable")     # accesses the html element holding the prompt
            result = {"success" : True,
                      "error" : None,
                      "data" : html[0].get_text()
                      }                            # accesses the prompt inside of the html element
        except IndexError:
            result = {"success" : False,
                      "error" : "IndexError",
                      "data" : "ERROR: No Prompt Found"}
        except Exception as e:
            result = {"success" : False,
                      "error" : e,
                      "data" : "ERROR: Unknown Error Occurred"
                      }

        return result

    def __str__(self):
        return "crodie"