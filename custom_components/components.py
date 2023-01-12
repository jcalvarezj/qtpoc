# Custom components with Qt Designer base

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox
from bson.json_util import dumps
from custom_components.ui_main import Ui_MainWindow
from custom_components.ui_dialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, mongoClient):
        super().__init__()
        self.mongoClient = mongoClient
        self.setupUi(self)

        self.btnQuery.pressed.connect(self.query_action)

    def query_action(self):
        found = None
        personas_collection = self.mongoClient.x.personas # Using database "x"

        search_field = ""

        if self.rbtId.isChecked():
            search_field = "cedula"
        if self.rbtFirstName.isChecked():
            search_field = "nombre"
        if self.rbtId.isChecked():
            search_field = "apellido"

        found = personas_collection.find({search_field: {"$regex": self.txtSearch.text(), "$options": "i"}})

        print(dumps(found))


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)