from tkinter import Tk, ttk

from c214_lab_project.application.ui.actions.home_actions import HomeActions
from c214_lab_project.application.ui.screens.base import BaseScreen


class Home(BaseScreen):
    def __init__(self, parent: Tk, *args, **kwargs) -> None:
        super(Home, self).__init__(parent, *args, **kwargs)

        self._upload_button = ttk.Button(
            self,
            text="Upload Image",
            command=lambda: HomeActions.choose_file_to_upload(
                self.set_filepath
            ),
        )
        self._upload_button.pack()

    def config_styles(self):
        self.configure(padding=32)

    def set_filepath(self, filepath):
        self._filepath = filepath
