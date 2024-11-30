from abc import abstractmethod
from tkinter import Tk, ttk


class BaseScreen(ttk.Frame):
    def __init__(self, parent: Tk, *args, **kwargs) -> None:
        self._parent = parent
        super(BaseScreen, self).__init__(*args, **kwargs)

        self.config_styles()

    @abstractmethod
    def config_styles(self):
        raise NotImplementedError()
