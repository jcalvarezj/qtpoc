import sys
from PySide6.QtWidgets import QApplication
from custom_components.components import MainWindow
from custom_components.components import Dialog
from pymongo import MongoClient


UI_FILE = "main.ui"
DB_HOST = "localhost"
DB_PORT = "27017"
DB_USER = "user"
DB_PASSWORD = "password"
DB_AUTH_DB = "admin"
DB_NAME = "x"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connection = None

    try:
        connection = MongoClient(f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authSource={DB_AUTH_DB}")
        connection[DB_NAME].command("ping")
    except Exception as e:
        dlg = Dialog()
        print(e)
        sys.exit(dlg.exec())

    window = MainWindow(connection, DB_NAME)
    window.show()

    sys.exit(app.exec())
