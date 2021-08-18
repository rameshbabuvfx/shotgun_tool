# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shotgunToolUI_Test.ui'
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
        MainWindow.resize(1201, 799)
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
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamily(u"Microsoft Sans Serif")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(164, 168, 174);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 3px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Microsoft Sans Serif")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:7px;\n"
"}")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(457, 16777215))
        self.verticalFrame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 7, 0)
        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(450, 300))
        self.label.setStyleSheet(u"QLabel{\n"
"	border-radius:50px;\n"
"}")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u"C:/Users/rames/Pictures/pexels-denys-gromov-7122719 (1).jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.treeWidget = QTreeWidget(self.verticalFrame)
        self.treeWidget.setObjectName(u"treeWidget")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        self.treeWidget.setFont(font3)
        self.treeWidget.setStyleSheet(u"QTreeWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QHeaderView:section {\n"
"	background-color: rgb(0, 0, 0);\n"
"    height:20px;                                \n"
"    border: 0px solid;\n"
"	border-radius:1px;\n"
"}")
        self.treeWidget.setFrameShape(QFrame.NoFrame)
        self.treeWidget.setFrameShadow(QFrame.Plain)
        self.treeWidget.header().setVisible(True)

        self.verticalLayout_2.addWidget(self.treeWidget)


        self.horizontalLayout_5.addWidget(self.verticalFrame)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(300, 30))
        font4 = QFont()
        font4.setFamily(u"Microsoft Sans Serif")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.pushButton_3)

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
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search your task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   Shotgun Tool", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.label.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

