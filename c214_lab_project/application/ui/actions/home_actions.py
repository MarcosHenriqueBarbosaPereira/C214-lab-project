from tkinter import filedialog
from typing import Callable


class HomeActions:
    @staticmethod
    def choose_file_to_upload(callback: Callable[[str], None]):
        chose_file = filedialog.askopenfilename(
            title="Select an file to upload"
        )

        callback(chose_file)
