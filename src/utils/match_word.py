class Match_Word:
    NUM_WORDS = 3

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
        valid_words = []

        for word in self.word_list:
            if word in self.dupes:
                continue
            if prompt in word:
                valid_words.append(word)
            if len(valid_words) >= self.NUM_WORDS:
                return valid_words
            
        return valid_words
    
    def update_dupes(self, duped_word):
        self.dupes.add(duped_word)
            
if __name__ == "__main__":
    bro = Match_Word()

    user_prompt = input("Enter a prompt: ")
    words = bro.get_word(user_prompt)

    print(words)