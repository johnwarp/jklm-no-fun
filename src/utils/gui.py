import tkinter as tk
import threading
import queue

# queue is used to safely communicate between threads since tkinter is not thread safe

class Gui:
    padding_x = 10
    padding_y = 20

    def __init__(self, root):
        self.root = root
        root.title("JKLM.nofun")

        self.q = queue.Queue()

        self.prompt = tk.Label(root, text="Press ctrl + alt + t to grab prompt", font=("Arial", 25))
        self.words = tk.Label(root, text="Possible words found here:\n\n\n", font=("Arial", 15))
        self.quit_button = tk.Button(root, text="Quit", font=("Arial", 10), width=25, command=root.destroy)

        self.prompt.pack(padx=self.padding_x, pady=self.padding_y)
        self.words.pack()
        self.quit_button.pack(padx=self.padding_x, pady=self.padding_y)

    def update(self, new_prompt, new_words_text):
        self.prompt.config(text=new_prompt)
        self.words.config(text=new_words_text)

    def process_queue(self):
        while not self.q.empty():
            prompt_dict = self.q.get_nowait()

            # parses the dict that includes the prompts and possible words
            new_prompt = prompt_dict["prompt"]
            new_words_list = prompt_dict["words"]
            new_words_text = "List of possible words:\n" + "\n".join(new_words_list)

            self.update(new_prompt, new_words_text)

    def schedule_update(self):
        self.root.after_idle(self.process_queue)

def user_input(gui):
    for _ in range(2):
        prompt = input("Input shit: ")
        prompt_dict = {"prompt" : prompt,
                       "words" : ["bruh", "bro", "brodie"]}
        gui.q.put(prompt_dict)
        gui.schedule_update()

if __name__ == "__main__":
    root = tk.Tk()
    bro = Gui(root)

    # takes user input and passes the info into a queue in the tkinter gui object in another thread
    input_thread = threading.Thread(target=user_input, args=(bro,), daemon=True)    # remember daemon=True
    input_thread.start()

    root.mainloop()