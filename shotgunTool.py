import os
import sys

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from shotgun_api3 import Shotgun


class Creator:
    def __init__(self):
        super().__init__()

        sg = Shotgun(
            "https://rock.shotgrid.autodesk.com/",
            "collector",
            "uoaboavygq4qlr_dicRunkxom"
        )

        data = {
            "project": {'type': 'Project', 'id': 122, 'name': 'Deamon'},
            "entity": {'type': 'Shot', 'id': 1174},
            "content": ""
        }
        for count, i in enumerate(range(30)):
            data["content"] = f"sh_00{count+1}"
            sg.create('Task', data=data)


if __name__ == '__main__':
    Creator()
