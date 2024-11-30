import webview


class Application:
    def __init__(self) -> None:
        pass

    def run(self):
        webview.settings["ALLOW_DOWNLOADS"] = True
        webview.settings["ALLOW_FILE_URLS"] = True
        webview.create_window("Upload File master", "./templates/index.html")
        webview.start()
