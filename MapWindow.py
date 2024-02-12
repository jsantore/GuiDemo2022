import io

from PySide6.QtWidgets import QWidget
import folium
from PySide6 import QtWebEngineWidgets


class Comp490MapWindow(QtWebEngineWidgets.QWebEngineView()):
    def __init__(self, data_to_display):
        super().__init__()
        self.data_to_display = data_to_display
        self.setup_window()

    def setup_window(self):
        """Initial demo a mangling of this answer from stackoverflow
        https://stackoverflow.com/questions/58590199/how-to-show-folium-map-inside-a-pyqt5-gui"""
        # what a terrible variable name - I might have to cite myself in a future class
        temp_demo_map = folium.Map(
            location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13
        )
        in_memory_file = io.BytesIO()
        temp_demo_map.save(in_memory_file)
        self.setHtml(in_memory_file.getvalue().decode("utf-8"))
        self.resize(800,600)
        self.show()
