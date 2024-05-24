from customtkinter import *
from tkVideoPlayer import TkinterVideo
from app import open_video


class Video(CTkFrame):
    def __init__(self, parent: CTk):
        super().__init__(self, master=parent)

        self.button = CTkButton(
            self, corner_radius=99, text="Upload A Video", command=self.open_video
        )

        self.vidplayer = TkinterVideo(self, True, True, True, bg="black")
        self.vidplayer.set_resampling_method(1)
        self.vidplayer.pack(expand=True, fill="both", padx=10, pady=10)
        self.vidplayer.bind("<<Duration>>", self.update_duration)
        self.vidplayer.bind("<<SecondChanged>>", self.update_scale)
        self.vidplayer.bind("<<Ended>>", self.video_ended)

        self.slider = CTkSlider(
            self, from_=-1, to=1, number_of_steps=1, command=self.seek
        )
        self.slider.set(-1)
        self.slider.pack(fill="both", padx=10, pady=10)

        self.play_pause_btn = CTkButton(
            master=self, text="Play ►", command=self.play_pause
        )
        self.play_pause_btn.pack(pady=10)

    def open_video(self):
        self.vid_player.stop()
        global video_file
        video_file = filedialog.askopenfilename(
            filetypes=[
                ("Video", ["*.mp4", "*.avi", "*.mov", "*.mkv", "*gif"]),
                ("All Files", "*.*"),
            ]
        )
        if video_file:
            try:
                self.vid_player.load(video_file)
                self.vid_player.play()
                self.progress_slider.set(-1)
                self.play_pause_btn.configure(text="Pause ||")
            except:
                print("Unable to load the file")
        pass

    def update_duration(self):
        try:
            duration = int(self.vid_player.video_info()["duration"])
            self.progress_slider.configure(
                from_=-1, to=duration, number_of_steps=duration
            )
        except:
            pass

    def update_scale(self):
        try:
            self.progress_slider.set(int(self.vid_player.current_duration()))
        except:
            pass

    def video_ended(self):
        self.play_pause_btn.configure(text="Play ►")
        self.progress_slider.set(-1)
        pass

    def seek(self):
        pass

    def play_pause(self):
        if video_file:
            if self.vid_player.is_paused():
                self.vid_player.play()
                self.play_pause_btn.configure(text="Pause ||")

            else:
                self.vid_player.pause()
                self.play_pause_btn.configure(text="Play ►")
        pass
