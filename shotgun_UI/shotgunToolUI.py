# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shotgunToolUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1364, 799)
        font = QFont()
        font.setStyleStrategy(QFont.NoAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SearchlineEdit = QLineEdit(self.centralwidget)
        self.SearchlineEdit.setObjectName(u"SearchlineEdit")
        self.SearchlineEdit.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamily(u"Microsoft Sans Serif")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.SearchlineEdit.setFont(font1)
        self.SearchlineEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(164, 168, 174);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 3px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.SearchlineEdit)

        self.ShotgunLabel = QLabel(self.centralwidget)
        self.ShotgunLabel.setObjectName(u"ShotgunLabel")
        font2 = QFont()
        font2.setFamily(u"Microsoft Sans Serif")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.ShotgunLabel.setFont(font2)
        self.ShotgunLabel.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:7px;\n"
"}")
        self.ShotgunLabel.setTextFormat(Qt.AutoText)
        self.ShotgunLabel.setScaledContents(False)

        self.horizontalLayout_4.addWidget(self.ShotgunLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.TasktableWidget = QTableWidget(self.centralwidget)
        if (self.TasktableWidget.columnCount() < 5):
            self.TasktableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TasktableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TasktableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TasktableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TasktableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TasktableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.TasktableWidget.rowCount() < 1):
            self.TasktableWidget.setRowCount(1)
        brush = QBrush(QColor(200, 25, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(brush);
        self.TasktableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TasktableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TasktableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TasktableWidget.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TasktableWidget.setItem(0, 4, __qtablewidgetitem9)
        self.TasktableWidget.setObjectName(u"TasktableWidget")
        self.TasktableWidget.setMinimumSize(QSize(711, 0))
        font3 = QFont()
        font3.setFamily(u"Microsoft Sans Serif")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.TasktableWidget.setFont(font3)
        self.TasktableWidget.setAutoFillBackground(False)
        self.TasktableWidget.setStyleSheet(u"QTableWidget{\n"
"	selection-background-color: rgb(91, 91, 91);\n"
"	background-color: rgb(30, 30, 30);\n"
"	alternate-background-color: rgb(18, 18, 18);\n"
"	color: rgb(198, 202, 208);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"	background-color: white;\n"
"	height: 7px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle{\n"
"	background-color: rgb(255, 112, 81);\n"
"    border-radius: 3px;\n"
"}")
        self.TasktableWidget.setFrameShape(QFrame.NoFrame)
        self.TasktableWidget.setFrameShadow(QFrame.Plain)
        self.TasktableWidget.setLineWidth(0)
        self.TasktableWidget.setMidLineWidth(1)
        self.TasktableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TasktableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TasktableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.TasktableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TasktableWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.TasktableWidget.setAlternatingRowColors(True)
        self.TasktableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.TasktableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.TasktableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.TasktableWidget.setShowGrid(False)
        self.TasktableWidget.setGridStyle(Qt.NoPen)
        self.TasktableWidget.setSortingEnabled(True)
        self.TasktableWidget.setCornerButtonEnabled(True)
        self.TasktableWidget.setRowCount(1)
        self.TasktableWidget.horizontalHeader().setVisible(True)
        self.TasktableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.TasktableWidget.horizontalHeader().setMinimumSectionSize(4)
        self.TasktableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.TasktableWidget.horizontalHeader().setHighlightSections(True)
        self.TasktableWidget.horizontalHeader().setStretchLastSection(False)
        self.TasktableWidget.verticalHeader().setVisible(False)
        self.TasktableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.TasktableWidget.verticalHeader().setMinimumSectionSize(0)
        self.TasktableWidget.verticalHeader().setDefaultSectionSize(35)
        self.TasktableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.TasktableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.TasktableWidget)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(457, 16777215))
        self.verticalFrame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 7, 0)
        self.ImageLabel = QLabel(self.verticalFrame)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMaximumSize(QSize(450, 300))
        self.ImageLabel.setStyleSheet(u"QLabel{\n"
"	border-radius:50px;\n"
"}")
        self.ImageLabel.setFrameShape(QFrame.NoFrame)
        self.ImageLabel.setPixmap(QPixmap(u"C:/Users/rames/Pictures/pexels-denys-gromov-7122719 (1).jpg"))
        self.ImageLabel.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.ImageLabel)

        self.TaskLoglistWidget = QListWidget(self.verticalFrame)
        self.TaskLoglistWidget.setObjectName(u"TaskLoglistWidget")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        self.TaskLoglistWidget.setFont(font4)
        self.TaskLoglistWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius:10px;\n"
"}")
        self.TaskLoglistWidget.setFrameShape(QFrame.NoFrame)
        self.TaskLoglistWidget.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.TaskLoglistWidget)


        self.horizontalLayout_5.addWidget(self.verticalFrame)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LoadTaskPushButton = QPushButton(self.centralwidget)
        self.LoadTaskPushButton.setObjectName(u"LoadTaskPushButton")
        self.LoadTaskPushButton.setMinimumSize(QSize(300, 30))
        font5 = QFont()
        font5.setFamily(u"Microsoft Sans Serif")
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.LoadTaskPushButton.setFont(font5)
        self.LoadTaskPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(30, 30, 30);\n"
"}")

        self.horizontalLayout_7.addWidget(self.LoadTaskPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SearchlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search your task", None))
        self.ShotgunLabel.setText(QCoreApplication.translate("MainWindow", u"   Shotgun Tool", None))
        ___qtablewidgetitem = self.TasktableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None));
        ___qtablewidgetitem1 = self.TasktableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Task Name", None));
        ___qtablewidgetitem2 = self.TasktableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.TasktableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Dead Line", None));
        ___qtablewidgetitem4 = self.TasktableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Task_ID", None));

        __sortingEnabled = self.TasktableWidget.isSortingEnabled()
        self.TasktableWidget.setSortingEnabled(False)
        self.TasktableWidget.setSortingEnabled(__sortingEnabled)

        self.ImageLabel.setText("")
        self.LoadTaskPushButton.setText(QCoreApplication.translate("MainWindow", u"Load Task", None))
    # retranslateUi

