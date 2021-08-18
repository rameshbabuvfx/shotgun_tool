import nuke
import shotgunTool

menu = nuke.toolbar("Nuke")
shotgun_menu = menu.addMenu("Shotgun Loader")
shotgun_menu.addCommand("Shotgun Loader", lambda: shotgunTool.main())
