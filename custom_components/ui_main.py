# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (QButtonGroup, QGridLayout, QGroupBox, QLabel,
                               QLineEdit, QListWidget, QMenuBar, QPushButton,
                               QRadioButton, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 521)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 481, 481))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 60, 251, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txtSearch = QLineEdit(self.verticalLayoutWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.verticalLayout.addWidget(self.txtSearch)

        self.lvwData = QListWidget(self.verticalLayoutWidget)
        self.lvwData.setObjectName(u"lvwData")

        self.verticalLayout.addWidget(self.lvwData)

        self.btnQuery = QPushButton(self.verticalLayoutWidget)
        self.btnQuery.setObjectName(u"btnQuery")

        self.verticalLayout.addWidget(self.btnQuery)

        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(300, 60, 161, 71))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rbtFirstName = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbtFirstName)
        self.rbtFirstName.setObjectName(u"rbtFirstName")
        self.rbtFirstName.setChecked(True)

        self.verticalLayout_3.addWidget(self.rbtFirstName)

        self.rbtLastName = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup.addButton(self.rbtLastName)
        self.rbtLastName.setObjectName(u"rbtLastName")

        self.verticalLayout_3.addWidget(self.rbtLastName)

        self.rbtId = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup.addButton(self.rbtId)
        self.rbtId.setObjectName(u"rbtId")

        self.verticalLayout_3.addWidget(self.rbtId)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(480, 0, 441, 131))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 30, 381, 79))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txtFirstName = QLineEdit(self.verticalLayoutWidget_2)
        self.txtFirstName.setObjectName(u"txtFirstName")

        self.gridLayout_3.addWidget(self.txtFirstName, 0, 2, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.txtLastName = QLineEdit(self.verticalLayoutWidget_2)
        self.txtLastName.setObjectName(u"txtLastName")

        self.gridLayout_3.addWidget(self.txtLastName, 1, 2, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.btnInsert = QPushButton(self.verticalLayoutWidget_2)
        self.btnInsert.setObjectName(u"btnInsert")

        self.verticalLayout_2.addWidget(self.btnInsert)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 923, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Query", None))
        self.btnQuery.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.rbtFirstName.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.rbtLastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.rbtId.setText(QCoreApplication.translate("MainWindow", u"Document Number", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.btnInsert.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
    # retranslateUi

