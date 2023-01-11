import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from pymongo import MongoClient


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

        self.btnQuery.pressed.connect(self.magic)

    def magic(self):
        print(self.mongoClient.admin.command("ping"))


if __name__ == "__main__":
    connection = MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authSource={DB_AUTH_DB}")

    app = QApplication(sys.argv)

    window = MainWindow(connection)
    window.show()

    sys.exit(app.exec())