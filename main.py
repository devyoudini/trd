from customtkinter import *
from tkVideoPlayer import TkinterVideo
from video import Video


class App(CTk):
    def __init__(self):
        super().__init__(self)
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.title("Traffic Violation Detection System")
        self.geometry("600x600")
        self.minsize(600, 600)

        self.frame = Video(self)

        self.mainloop()


App()
