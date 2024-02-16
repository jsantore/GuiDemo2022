import io

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QVBoxLayout
import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class Comp490MapWindow(QWidget):
    def __init__(self, data_to_display):
        super().__init__()
        self.data_to_display = data_to_display
        #self.map = self.build_map()
        self.setup_window()

    def setup_window(self):
        self.layout = QVBoxLayout(self)
        self.webview = QWebEngineView()
        """Initial demo a mangling of this answer from stackoverflow
                https://stackoverflow.com/questions/58590199/how-to-show-folium-map-inside-a-pyqt5-gui"""
        # what a terrible variable name - I might have to cite myself in a future class
        temp_demo_map = folium.Map(
            location=[45.5236, -122.6750], zoom_start=13
        )
        in_memory_file = io.BytesIO()
        temp_demo_map.save(in_memory_file, close_file=False)
        self.webview.setHtml(in_memory_file.getvalue().decode("utf-8"))
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        self.resize(800, 800)
        self.show()


