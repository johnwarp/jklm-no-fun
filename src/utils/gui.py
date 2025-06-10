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

        self.prompt_text = "Press ctrl + alt + t to grab prompt"
        words_list = ["cock", "ball", "torture"]
        self.words_text = "List of possible words:\n" + "\n".join(words_list)

        self.prompt = tk.Label(root, text=self.prompt_text, font=("Arial", 25))
        self.words = tk.Label(root, text=self.words_text, font=("Arial", 15))
        self.quit_button = tk.Button(root, text="Quit", font=("Arial", 10), width=25, command=root.destroy)

        self.prompt.pack(padx=self.padding_x, pady=self.padding_y)
        self.words.pack()
        self.quit_button.pack(padx=self.padding_x, pady=self.padding_y)

    def update(self, new_prompt):
        self.prompt.config(text=new_prompt)

    def process_queue(self):
        while not self.q.empty():
            new_prompt = self.q.get_nowait()
            self.update(new_prompt)

    def schedule_update(self):
        self.root.after_idle(self.process_queue)

    def quit(self):
        self.root.destroy()
        print("window destroyed")

def user_input(gui):
    for _ in range(4):
        prompt = input()
        gui.q.put(prompt)
        gui.schedule_update()


if __name__ == "__main__":
    root = tk.Tk()
    bro = Gui(root)

    def start_input_thread():
        # takes user input and passes the info into a queue in the tkinter gui object in another thread
        input_thread = threading.Thread(target=user_input, args=(bro,))
        input_thread.start()

    root.after(100, start_input_thread)

    root.mainloop()