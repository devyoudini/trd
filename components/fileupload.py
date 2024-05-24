from customtkinter import *


class FileUpload(CTkFrame):
    def __init__(self, parent: CTk):
        super().__init__(parent)

        self.label = CTkLabel(self, text="Upload  File")
        self.label.grid(row=0, column=0, padx=20)
