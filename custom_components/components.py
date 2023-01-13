# Custom components with Qt Designer base

from PySide6.QtWidgets import QMainWindow, QDialog, QErrorMessage
from bson.json_util import dumps
from custom_components.ui_main import Ui_MainWindow
from custom_components.ui_dialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, mongo_client, db_name):
        super().__init__()
        self.mongo_client = mongo_client
        self.db_name = db_name
        self.setupUi(self)

        self.btn_query.pressed.connect(self.query_action)
        self.btn_insert.pressed.connect(self.insert_action)

    def query_action(self):
        self.lvwData.clear()

        found = None
        personas_collection = self.mongo_client[self.db_name].personas

        search_field = ""

        if self.rbt_id.isChecked():
            search_field = "cedula"
        if self.rbt_first_name.isChecked():
            search_field = "nombre"
        if self.rbt_last_name.isChecked():
            search_field = "apellido"

        found = personas_collection.find({search_field: {"$regex": self.txtSearch.text(), "$options": "i"}})

        for person in found:
            self.lvwData.addItem(f"{person['nombre']} {person['apellido']} ({person['cedula']})")

    def insert_action(self):
        personas_collection = self.mongo_client[self.db_name].personas

        try:
            personas_collection.insert_one({
                "nombre": self.txt_first_name.text(),
                "apellido": self.txt_last_name.text(),
                "cedula": self.txt_id.text()
            })
        except Exception as e:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Oh no! - ' + e)



class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
