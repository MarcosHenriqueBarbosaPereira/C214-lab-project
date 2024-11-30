from tkinter import Tk, ttk

import sv_ttk

from c214_lab_project.application.ui.screens import Home, SignIn


class Application:
    def __init__(self) -> None:
        self._root = Tk(screenName="Master Upload Storage")

        self._root.title("Master Upload Storage")
        self._root.geometry("1280x720")

        self._frames = {
            "home": Home(parent=self),
            "sign_in": SignIn(parent=self),
        }

        for frame in self._frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.navigate_to("sign_in")
        self._config_theme()

    def run(self):
        self._root.mainloop()

    def _config_theme(self):
        sv_ttk.set_theme("dark")

    def navigate_to(self, screen_name: str):
        screen = self._frames[screen_name]
        screen.tkraise()
