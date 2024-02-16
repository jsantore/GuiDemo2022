from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QVBoxLayout

class Comp490MapWindow(QWidget):
    def __init__(self, data_to_display):
        super().__init__()
        self.data_to_display = data_to_display
        #self.map = self.build_map()
        self.setup_window()

    def setup_window(self):
        self.layout = QVBoxLayout(self)
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.python.org/"))
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        self.resize(800, 800)
        self.show()