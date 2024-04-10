from design import Ui_MainWindow
from db_functions import *
from api import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPixmap
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.points = []
        self.types = get_transport_types_from_db()
        self.transport_combo_box.addItems(self.types)
        self.matters = get_matter_from_db()
        self.matter_combo_box.addItems(self.matters)
        self.get_routes_button.clicked.connect(self.print_info)
        self.draw_route_button.clicked.connect(self.print_image)
        self.scale_Slider.setMaximum(20)
        self.scale_Slider.setMinimum(10)
        self.scale_Slider.valueChanged.connect(self.update_map)

    def print_info(self):
        t = self.transport_combo_box.currentText()
        m = self.matter_combo_box.currentText()
        self.routes = get_routes_info_from_db(t, m)
        self.listWidget.clear()
        routes = [x[1] + '; ' + x[2] for x in self.routes]
        self.listWidget.addItems(routes)

    def find_id(self, d):
        for route in self.routes:
            if route[1] == d:
                return route[0]

    def print_image(self):
        d = self.listWidget.currentItem()
        if not d:
            return
        d = d.text().split('; ')[0]
        this_id = self.find_id(d)
        self.points = get_points_by_id_from_db(this_id)
        self.points = transform_from_dp_to_api(self.points)
        picture = get_map(self.points)
        pixmap = QPixmap()
        pixmap.loadFromData(picture)
        self.label_4.setPixmap(pixmap)
        self.update()

    def update_map(self):
        x = self.scale_Slider.value()
        picture = get_map(self.points, z=x)
        pixmap = QPixmap()
        pixmap.loadFromData(picture)
        self.label_4.setPixmap(pixmap)
        self.update()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec_())