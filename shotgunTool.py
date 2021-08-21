import os
import sys
from pprint import pprint

from PySide2.QtWidgets import *
from shotgun_api3 import Shotgun

from shotgun_UI import shotgunToolUI


class ShotgunLoader(QMainWindow, shotgunToolUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user = "tommy oliver"
        self.task_data = None
        header = self.TasktableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.sg = Shotgun(
            "https://rock.shotgrid.autodesk.com/",
            "collector",
            "uoaboavygq4qlr_dicRunkxom"
        )
        self.get_task_data()
        self.populate_task_data()

    def get_task_data(self):
        self.task_data = self.sg.find(
            "Task",
            [["task_assignees", "is", {"type": "HumanUser", "id": 121}]],
            ["content", "sg_status_list", "sg_description", "due_date"]
        )

    def populate_task_data(self):
        row_count = len(self.task_data)
        print(row_count)
        self.TasktableWidget.setRowCount(row_count)


def main():
    main.tool = ShotgunLoader()
    main.tool.show()


if __name__ == '__main__':
    app = QApplication()
    loader = ShotgunLoader()
    loader.show()
    sys.exit(app.exec_())
