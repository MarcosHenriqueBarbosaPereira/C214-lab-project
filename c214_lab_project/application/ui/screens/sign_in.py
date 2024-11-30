from tkinter import messagebox, ttk

from c214_lab_project.application.ui.screens.base import BaseScreen


class SignIn(BaseScreen):
    def __init__(self, parent, *args, **kwargs) -> None:
        super(SignIn, self).__init__(parent, *args, **kwargs)

        self.username_label = ttk.Label(self, text="Usuário:")
        self.username_label.pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        self.password_label = ttk.Label(self, text="Senha:")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = ttk.Button(
            self, text="Login", command=self.process_login
        )
        self.login_button.pack()

    def process_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self._parent.navigate_to("home")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def config_styles(self):
        self.configure(padding=32)
