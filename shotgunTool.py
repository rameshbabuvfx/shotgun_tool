import os
import sys

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from shotgun_api3 import Shotgun

from shotgun_UI import shotgunToolUI


class ShotgunLoader(QMainWindow, shotgunToolUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        sg = Shotgun(
            "https://rock.shotgrid.autodesk.com/",
            "collector",
            "uoaboavygq4qlr_dicRunkxom"
        )


def main():
    main.tool = ShotgunLoader()
    main.tool.show()


if __name__ == '__main__':
    app = QApplication()
    loader = ShotgunLoader()
    loader.show()
    sys.exit(app.exec_())
