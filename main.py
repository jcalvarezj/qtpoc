import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from pymongo import MongoClient
from bson.json_util import dumps


UI_FILE = "main.ui"
DB_HOST = "localhost"
DB_PORT = "27017"
DB_USER = "user"
DB_PASSWORD = "password"
DB_AUTH_DB = "admin"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, mongoClient: MongoClient):
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


if __name__ == "__main__":
    connection = MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authSource={DB_AUTH_DB}")

    app = QApplication(sys.argv)

    window = MainWindow(connection)
    window.show()

    sys.exit(app.exec())
