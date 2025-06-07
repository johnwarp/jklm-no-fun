class Match_Word:
    def __init__(self):
        # initialize a list with all the words in the word bank text file
        with open("src/data/word_bank.txt", "r") as file:
            self.word_list = [line.rstrip() for line in file]

        self.word_list.sort(key=len)
        
        # set that includes duplicate words already used
        self.dupes = {}
    
    # TODO return a list include multiple words incase other players have already used that word
    def get_word(self, prompt):
        prompt = prompt.upper()
        for word in self.word_list:
            if prompt in word:
                return word
            
if __name__ == "__main__":
    bro = Match_Word()
    word = bro.get_word("bro")

    print(word)