import tkinter as tk

class Gui:
    padding_x = 20
    padding_y = 20

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JKLM.nofun")

        self.prompt_text = "Press ctrl + alt + t to grab prompt"
        self.possible_words = []

        self.prompt = tk.Label(self.root, text=self.prompt_text, font=("Arial", 25))
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 10), width=25, command=self.quit)

        self.prompt.pack(padx=self.padding_x, pady=self.padding_y)
        self.quit_button.pack(padx=self.padding_x, pady=self.padding_y)

    def quit(self):
        self.root.destroy()
        print("window destroyed")

    def update(self, new_prompt):
        self.prompt.config(text=new_prompt)

    def run(self):
        self.root.mainloop()    

if __name__ == "__main__":
    bro = Gui()

    prompt = "bro"

    while prompt != "crodie":

        prompt = input("Enter a prompt: ")

        bro.update(prompt)
        print("updated")
        
        bro.run()

    print('ending program')