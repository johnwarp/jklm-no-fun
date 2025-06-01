import tkinter as tk

class Gui:
    padding_x = 20
    padding_y = 20

    def __init__(self, prompt_text):
        self.root = tk.Tk()
        self.prompt_text = prompt_text
        self.prompt = tk.Label(self.root, text=self.prompt_text, font=("Arial", 25))

        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 10), width=25, command=self.root.destroy)

    def run(self):
        self.prompt.pack(padx=self.padding_x, pady=self.padding_y)
        self.quit_button.pack(padx=self.padding_x, pady=self.padding_y)