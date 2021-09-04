import os
import sys
from pprint import pprint

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from shotgun_api3 import Shotgun

from shotgun_UI import shotgunToolUI
import Icons


class ShotgunLoader(QMainWindow, shotgunToolUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.sg = Shotgun(
        #     "https://rock.shotgrid.autodesk.com/",
        #     "collector",
        #     "uoaboavygq4qlr_dicRunkxom"
        # )
        self.sg = Shotgun(
            "https://rcvfx.shotgunstudio.com/",
            "shotgun_testing_review",
            "qz7d@peancfQvbymnantdmjpt"
        )

        self.setupUi(self)
        self.user = "tommy oliver"
        self.tasks_data = None

        h_header = self.TasktableWidget.horizontalHeader()
        h_header.setSectionResizeMode(QHeaderView.Stretch)
        h_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        h_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.TasktableWidget.resizeColumnsToContents()
        self.TasktableWidget.setFocusPolicy(Qt.NoFocus)

        self.get_task_data()
        self.populate_task_data()

    def get_task_data(self):
        self.tasks_data = self.sg.find(
            "Task",
            [["task_assignees", "is", {"type": "HumanUser", "id": 1892}]],
            ["content", "sg_status_list", "sg_description", "due_date"]
        )

    def populate_task_data(self):
        row_count = len(self.tasks_data)
        self.TasktableWidget.setRowCount(row_count)

        for count, task_data in enumerate(self.tasks_data):
            self.TasktableWidget.setMinimumHeight(150)

            self.thumbnail_label = QLabel()
            self.thumbnail_label.setMaximumWidth(170)
            self.thumbnail_label.setMaximumHeight(100)
            self.thumbnail_label.setScaledContents(True)
            self.thumbnail_label.setPixmap(
                QPixmap(r"D:\PythonProjects\PYTHON_scripts\shotgun_tool\Icons\NoImage.png")
            )
            self.TasktableWidget.setCellWidget(count, 0, self.thumbnail_label)

            task_item = QTableWidgetItem(task_data["content"])
            task_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.TasktableWidget.setItem(count, 1, task_item)

            task_status = QTableWidgetItem(task_data["sg_status_list"])
            task_status.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.TasktableWidget.setItem(count, 2, task_status)

            # task_description = QTableWidgetItem(task_data["sg_description"])
            # task_description.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            # self.TasktableWidget.setItem(count, 3, task_description)

            due_date = QTableWidgetItem(task_data["due_date"])
            due_date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.TasktableWidget.setItem(count, 3, due_date)

            task_id = QTableWidgetItem(task_data["id"])
            task_id.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.TasktableWidget.setItem(count, 4, task_id)
            self.TasktableWidget.setWordWrap(True)
            self.TasktableWidget.resizeRowsToContents()



def main():
    main.tool = ShotgunLoader()
    main.tool.show()


if __name__ == '__main__':
    app = QApplication()
    loader = ShotgunLoader()
    loader.show()
    sys.exit(app.exec_())


"""
{'content': 'sh_001_Roto_5962',
  'due_date': '2010-05-05',
  'id': 5962,
  'sg_description': None,
  'sg_status_list': 'wtg',
  'type': 'Task'},
  """