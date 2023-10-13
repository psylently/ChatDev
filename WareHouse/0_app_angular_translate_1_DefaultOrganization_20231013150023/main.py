'''
This is the main file of the web application.
'''
from tkinter import Tk, Button, Label, filedialog
from translator import Translator
class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("File Translator")
        self.label = Label(root, text="Select a text file to translate:")
        self.label.pack()
        self.button = Button(root, text="Browse", command=self.browse_file)
        self.button.pack()
        self.translator = Translator()
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.translate_file(file_path)
    def translate_file(self, file_path):
        translated_text = self.translator.translate(file_path)
        self.display_translation(translated_text)
    def display_translation(self, translated_text):
        self.label.config(text=translated_text)
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()