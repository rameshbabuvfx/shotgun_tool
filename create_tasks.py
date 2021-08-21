from shotgun_api3 import Shotgun
import pprint

sg = Shotgun(
    "https://rock.shotgrid.autodesk.com/",
    "collector",
    "uoaboavygq4qlr_dicRunkxom"
)

task_list = sg.find("Task", [["task_assignees", "is", {"type": "HumanUser", "id": 134}]])
print(task_list)
