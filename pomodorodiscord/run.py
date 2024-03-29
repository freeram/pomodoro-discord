import customtkinter as ctk
from src.pomodoro_frame import PomodoroFrame
from src.settings_frame import SettingsFrame
from src.stats_frame import StatsFrame
from src.utils import load_config


class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Main")
        self.add("Settings")
        self.add("Stats")

        self.main_frame = PomodoroFrame(self.tab("Main"))
        self.main_frame.pack(expand=True, fill='both')

        self.settings_frame = SettingsFrame(self.tab("Settings"))
        self.settings_frame.pack(expand=True, fill='both')

        self.stats_frame = StatsFrame(self.tab("Stats"))
        self.stats_frame.pack(expand=True, fill='both')


class PomodoroApp(ctk.CTk):
    WIDTH = 350
    HEIGHT = 400

    def __init__(self):
        super().__init__()

        self.title("Pomodoro Tracker")
        self.geometry(f"{PomodoroApp.WIDTH}x{PomodoroApp.HEIGHT}")

        self.tabview = TabView(master=self)
        self.tabview.pack(pady=(15, 30), expand=True, fill='y')


if __name__ == "__main__":
    config = load_config()
    ctk.set_default_color_theme(f"themes/{config['theme']}.json")
    ctk.set_appearance_mode("dark")
    app = PomodoroApp()
    app.mainloop()
