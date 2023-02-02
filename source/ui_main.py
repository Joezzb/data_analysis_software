# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        MainWindow.resize(1107, 873)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0, 0, 50);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(0, 0, 50);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(0, 0, 50);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon4)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_bug = QPushButton(self.frame_bug)
        self.bn_bug.setObjectName(u"bn_bug")
        self.bn_bug.setMinimumSize(QSize(80, 55))
        self.bn_bug.setMaximumSize(QSize(160, 55))
        self.bn_bug.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/bugAsset 47.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_bug.setIcon(icon5)
        self.bn_bug.setIconSize(QSize(22, 22))
        self.bn_bug.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_bug)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_cloud = QPushButton(self.frame_cloud)
        self.bn_cloud.setObjectName(u"bn_cloud")
        self.bn_cloud.setMinimumSize(QSize(80, 55))
        self.bn_cloud.setMaximumSize(QSize(160, 55))
        self.bn_cloud.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/cloudAsset 48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_cloud.setIcon(icon6)
        self.bn_cloud.setIconSize(QSize(22, 12))
        self.bn_cloud.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_cloud)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_android)
        self.bn_android.setObjectName(u"bn_android")
        self.bn_android.setMinimumSize(QSize(80, 55))
        self.bn_android.setMaximumSize(QSize(160, 55))
        self.bn_android.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/androidAsset 49.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android.setIcon(icon7)
        self.bn_android.setIconSize(QSize(20, 22))
        self.bn_android.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_android)


        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(255,255,255);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setStyleSheet(u"color:rgb(0,0,0);")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame_home_main)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.graphviews = QGraphicsView(self.frame_home_main)
        self.graphviews.setObjectName(u"graphviews")
        self.graphviews.setMinimumSize(QSize(470, 350))
        self.graphviews.setMaximumSize(QSize(3000, 3000))

        self.gridLayout_7.addWidget(self.graphviews, 0, 0, 1, 4)

        self.label_home_1 = QLabel(self.frame_home_main)
        self.label_home_1.setObjectName(u"label_home_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_home_1.sizePolicy().hasHeightForWidth())
        self.label_home_1.setSizePolicy(sizePolicy)
        self.label_home_1.setMinimumSize(QSize(120, 30))
        self.label_home_1.setMaximumSize(QSize(200, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.label_home_1.setFont(font)
        self.label_home_1.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_7.addWidget(self.label_home_1, 1, 0, 1, 1)

        self.label_home_4 = QLabel(self.frame_home_main)
        self.label_home_4.setObjectName(u"label_home_4")
        sizePolicy.setHeightForWidth(self.label_home_4.sizePolicy().hasHeightForWidth())
        self.label_home_4.setSizePolicy(sizePolicy)
        self.label_home_4.setMinimumSize(QSize(120, 30))
        self.label_home_4.setMaximumSize(QSize(200, 30))
        self.label_home_4.setFont(font)
        self.label_home_4.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_7.addWidget(self.label_home_4, 2, 2, 1, 1)

        self.line_home_2 = QLineEdit(self.frame_home_main)
        self.line_home_2.setObjectName(u"line_home_2")
        self.line_home_2.setEnabled(False)
        self.line_home_2.setMinimumSize(QSize(115, 32))
        self.line_home_2.setMaximumSize(QSize(400, 32))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.line_home_2.setFont(font1)
        self.line_home_2.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_7.addWidget(self.line_home_2, 1, 3, 1, 1)

        self.line_home_3 = QLineEdit(self.frame_home_main)
        self.line_home_3.setObjectName(u"line_home_3")
        self.line_home_3.setEnabled(False)
        self.line_home_3.setMinimumSize(QSize(115, 32))
        self.line_home_3.setMaximumSize(QSize(400, 32))
        self.line_home_3.setFont(font1)
        self.line_home_3.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_7.addWidget(self.line_home_3, 2, 3, 1, 1)

        self.line_home_4 = QLineEdit(self.frame_home_main)
        self.line_home_4.setObjectName(u"line_home_4")
        self.line_home_4.setEnabled(False)
        self.line_home_4.setMinimumSize(QSize(115, 32))
        self.line_home_4.setMaximumSize(QSize(400, 32))
        self.line_home_4.setFont(font1)
        self.line_home_4.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_7.addWidget(self.line_home_4, 2, 1, 1, 1)

        self.line_home_1 = QLineEdit(self.frame_home_main)
        self.line_home_1.setObjectName(u"line_home_1")
        self.line_home_1.setEnabled(False)
        self.line_home_1.setMinimumSize(QSize(115, 32))
        self.line_home_1.setMaximumSize(QSize(400, 32))
        self.line_home_1.setFont(font1)
        self.line_home_1.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_7.addWidget(self.line_home_1, 1, 1, 1, 1)

        self.label_home_2 = QLabel(self.frame_home_main)
        self.label_home_2.setObjectName(u"label_home_2")
        sizePolicy.setHeightForWidth(self.label_home_2.sizePolicy().hasHeightForWidth())
        self.label_home_2.setSizePolicy(sizePolicy)
        self.label_home_2.setMinimumSize(QSize(120, 30))
        self.label_home_2.setMaximumSize(QSize(200, 30))
        self.label_home_2.setFont(font)
        self.label_home_2.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_7.addWidget(self.label_home_2, 1, 2, 1, 1)

        self.label_home_3 = QLabel(self.frame_home_main)
        self.label_home_3.setObjectName(u"label_home_3")
        sizePolicy.setHeightForWidth(self.label_home_3.sizePolicy().hasHeightForWidth())
        self.label_home_3.setSizePolicy(sizePolicy)
        self.label_home_3.setMinimumSize(QSize(120, 30))
        self.label_home_3.setMaximumSize(QSize(200, 30))
        self.label_home_3.setFont(font)
        self.label_home_3.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_7.addWidget(self.label_home_3, 2, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_home_stat)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        sizePolicy.setHeightForWidth(self.lab_home_stat_hed.sizePolicy().hasHeightForWidth())
        self.lab_home_stat_hed.setSizePolicy(sizePolicy)
        self.lab_home_stat_hed.setMinimumSize(QSize(200, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(200, 55))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semilight")
        font2.setPointSize(24)
        self.lab_home_stat_hed.setFont(font2)
        self.lab_home_stat_hed.setStyleSheet(u"color:rgb(0,0,0);")
        self.lab_home_stat_hed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.lab_home_stat_hed, 0, 0, 1, 1)

        self.overview_dataset = QPushButton(self.frame_home_stat)
        self.overview_dataset.setObjectName(u"overview_dataset")
        self.overview_dataset.setMinimumSize(QSize(200, 30))
        self.overview_dataset.setMaximumSize(QSize(300, 30))
        self.overview_dataset.setFont(font1)
        self.overview_dataset.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.overview_dataset.setCheckable(False)
        self.overview_dataset.setFlat(True)

        self.gridLayout_8.addWidget(self.overview_dataset, 1, 0, 1, 1)

        self.dataname = QComboBox(self.frame_home_stat)
        self.dataname.addItem("")
        self.dataname.setObjectName(u"dataname")
        self.dataname.setMinimumSize(QSize(200, 30))
        self.dataname.setMaximumSize(QSize(400, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.dataname.setFont(font3)
        self.dataname.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"")
        self.dataname.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.dataname.setFrame(False)
        self.dataname.setModelColumn(0)

        self.gridLayout_8.addWidget(self.dataname, 2, 0, 1, 1)

        self.rownumber = QComboBox(self.frame_home_stat)
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.addItem("")
        self.rownumber.setObjectName(u"rownumber")
        self.rownumber.setMinimumSize(QSize(200, 30))
        self.rownumber.setMaximumSize(QSize(400, 30))
        self.rownumber.setFont(font3)
        self.rownumber.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"")
        self.rownumber.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.rownumber.setFrame(False)
        self.rownumber.setModelColumn(0)

        self.gridLayout_8.addWidget(self.rownumber, 3, 0, 1, 1)

        self.overview_model = QPushButton(self.frame_home_stat)
        self.overview_model.setObjectName(u"overview_model")
        self.overview_model.setMinimumSize(QSize(200, 30))
        self.overview_model.setMaximumSize(QSize(300, 30))
        self.overview_model.setFont(font1)
        self.overview_model.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.overview_model.setCheckable(False)
        self.overview_model.setFlat(True)

        self.gridLayout_8.addWidget(self.overview_model, 4, 0, 1, 1)

        self.modelname = QComboBox(self.frame_home_stat)
        self.modelname.addItem("")
        self.modelname.setObjectName(u"modelname")
        self.modelname.setMinimumSize(QSize(200, 30))
        self.modelname.setMaximumSize(QSize(400, 30))
        self.modelname.setFont(font3)
        self.modelname.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"\n"
"")
        self.modelname.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.modelname.setFrame(False)
        self.modelname.setModelColumn(0)

        self.gridLayout_8.addWidget(self.modelname, 5, 0, 1, 1)

        self.overview_predict = QPushButton(self.frame_home_stat)
        self.overview_predict.setObjectName(u"overview_predict")
        self.overview_predict.setMinimumSize(QSize(200, 30))
        self.overview_predict.setMaximumSize(QSize(300, 30))
        self.overview_predict.setFont(font1)
        self.overview_predict.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.overview_predict.setCheckable(False)
        self.overview_predict.setFlat(True)

        self.gridLayout_8.addWidget(self.overview_predict, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 193, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 7, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(255);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(24)
        self.lab_about_home.setFont(font4)
        self.lab_about_home.setStyleSheet(u"color:rgb(0);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)

        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(255);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_cloud)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(30)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color:rgb(0,0,0);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(255);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(255);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug = QWidget()
        self.page_bug.setObjectName(u"page_bug")
        self.page_bug.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_Bug = QLabel(self.page_bug)
        self.lab_Bug.setObjectName(u"lab_Bug")
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        self.lab_Bug.setFont(font2)
        self.lab_Bug.setStyleSheet(u"color:rgb(0,0,0);")
        self.lab_Bug.setMargin(3)

        self.verticalLayout_7.addWidget(self.lab_Bug)

        self.frame_bug_main = QFrame(self.page_bug)
        self.frame_bug_main.setObjectName(u"frame_bug_main")
        self.frame_bug_main.setMinimumSize(QSize(0, 200))
        self.frame_bug_main.setMaximumSize(QSize(16777215, 200))
        self.frame_bug_main.setFrameShape(QFrame.NoFrame)
        self.frame_bug_main.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_bug_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.analyst_traindata = QPushButton(self.frame_bug_main)
        self.analyst_traindata.setObjectName(u"analyst_traindata")
        self.analyst_traindata.setMinimumSize(QSize(225, 30))
        self.analyst_traindata.setMaximumSize(QSize(400, 30))
        self.analyst_traindata.setFont(font1)
        self.analyst_traindata.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.analyst_traindata.setCheckable(False)
        self.analyst_traindata.setFlat(True)

        self.gridLayout.addWidget(self.analyst_traindata, 0, 0, 1, 1)

        self.analyst_trainname = QComboBox(self.frame_bug_main)
        self.analyst_trainname.addItem("")
        self.analyst_trainname.addItem("")
        self.analyst_trainname.addItem("")
        self.analyst_trainname.addItem("")
        self.analyst_trainname.addItem("")
        self.analyst_trainname.setObjectName(u"analyst_trainname")
        self.analyst_trainname.setMinimumSize(QSize(225, 30))
        self.analyst_trainname.setMaximumSize(QSize(400, 30))
        self.analyst_trainname.setFont(font3)
        self.analyst_trainname.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"\n"
"")
        self.analyst_trainname.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.analyst_trainname.setFrame(False)
        self.analyst_trainname.setModelColumn(0)

        self.gridLayout.addWidget(self.analyst_trainname, 1, 0, 1, 1)

        self.analyst_model = QComboBox(self.frame_bug_main)
        self.analyst_model.addItem("")
        self.analyst_model.addItem("")
        self.analyst_model.addItem("")
        self.analyst_model.addItem("")
        self.analyst_model.addItem("")
        self.analyst_model.setObjectName(u"analyst_model")
        self.analyst_model.setMinimumSize(QSize(225, 30))
        self.analyst_model.setMaximumSize(QSize(400, 30))
        self.analyst_model.setFont(font3)
        self.analyst_model.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"")
        self.analyst_model.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.analyst_model.setFrame(False)
        self.analyst_model.setModelColumn(0)

        self.gridLayout.addWidget(self.analyst_model, 1, 1, 1, 1)

        self.analyst_train = QPushButton(self.frame_bug_main)
        self.analyst_train.setObjectName(u"analyst_train")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.analyst_train.sizePolicy().hasHeightForWidth())
        self.analyst_train.setSizePolicy(sizePolicy1)
        self.analyst_train.setMinimumSize(QSize(225, 30))
        self.analyst_train.setMaximumSize(QSize(400, 30))
        self.analyst_train.setFont(font1)
        self.analyst_train.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.analyst_train.setCheckable(False)
        self.analyst_train.setFlat(True)

        self.gridLayout.addWidget(self.analyst_train, 1, 2, 1, 1)

        self.analyst_savepath = QLineEdit(self.frame_bug_main)
        self.analyst_savepath.setObjectName(u"analyst_savepath")
        sizePolicy1.setHeightForWidth(self.analyst_savepath.sizePolicy().hasHeightForWidth())
        self.analyst_savepath.setSizePolicy(sizePolicy1)
        self.analyst_savepath.setMinimumSize(QSize(450, 30))
        self.analyst_savepath.setMaximumSize(QSize(800, 30))

        self.gridLayout.addWidget(self.analyst_savepath, 2, 0, 1, 2)

        self.analyst_save = QPushButton(self.frame_bug_main)
        self.analyst_save.setObjectName(u"analyst_save")
        self.analyst_save.setMinimumSize(QSize(225, 30))
        self.analyst_save.setMaximumSize(QSize(400, 30))
        self.analyst_save.setFont(font1)
        self.analyst_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.analyst_save.setCheckable(False)
        self.analyst_save.setFlat(True)

        self.gridLayout.addWidget(self.analyst_save, 2, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_bug_main)

        self.textBrowser = QTextBrowser(self.page_bug)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.page_bug)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.page_table.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout_5 = QVBoxLayout(self.page_table)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.page_table)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(700, 460))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_line = QLineEdit(self.frame_2)
        self.table_line.setObjectName(u"table_line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_line.sizePolicy().hasHeightForWidth())
        self.table_line.setSizePolicy(sizePolicy3)
        self.table_line.setMinimumSize(QSize(200, 30))
        self.table_line.setMaximumSize(QSize(1000, 30))

        self.gridLayout_2.addWidget(self.table_line, 0, 0, 1, 1)

        self.table_search = QPushButton(self.frame_2)
        self.table_search.setObjectName(u"table_search")
        self.table_search.setMinimumSize(QSize(150, 30))
        self.table_search.setMaximumSize(QSize(400, 30))
        self.table_search.setFont(font1)
        self.table_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.table_search.setCheckable(False)
        self.table_search.setFlat(True)

        self.gridLayout_2.addWidget(self.table_search, 0, 1, 1, 1)

        self.table_mode = QComboBox(self.frame_2)
        self.table_mode.addItem("")
        self.table_mode.addItem("")
        self.table_mode.addItem("")
        self.table_mode.setObjectName(u"table_mode")
        self.table_mode.setMinimumSize(QSize(150, 30))
        self.table_mode.setMaximumSize(QSize(400, 30))
        self.table_mode.setFont(font3)
        self.table_mode.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(0,0,50);\n"
"}\n"
"\n"
"")
        self.table_mode.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.table_mode.setFrame(False)
        self.table_mode.setModelColumn(0)

        self.gridLayout_2.addWidget(self.table_mode, 0, 2, 1, 1)

        self.table_delete = QPushButton(self.frame_2)
        self.table_delete.setObjectName(u"table_delete")
        self.table_delete.setMinimumSize(QSize(150, 30))
        self.table_delete.setMaximumSize(QSize(400, 30))
        self.table_delete.setFont(font1)
        self.table_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0,0,50);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,0,50);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,0,255);\n"
"	background-color: rgb(0,0,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.table_delete.setCheckable(False)
        self.table_delete.setFlat(True)

        self.gridLayout_2.addWidget(self.table_delete, 0, 3, 1, 1)

        self.eventtable = QTableWidget(self.frame_2)
        if (self.eventtable.columnCount() < 4):
            self.eventtable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.eventtable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.eventtable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.eventtable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.eventtable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.eventtable.setObjectName(u"eventtable")
        sizePolicy2.setHeightForWidth(self.eventtable.sizePolicy().hasHeightForWidth())
        self.eventtable.setSizePolicy(sizePolicy2)
        self.eventtable.setMinimumSize(QSize(680, 400))
        self.eventtable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.eventtable, 1, 0, 1, 4)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_table)
        self.page_android = QWidget()
        self.page_android.setObjectName(u"page_android")
        self.page_android.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout_9 = QVBoxLayout(self.page_android)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_android)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_v1 = QLabel(self.frame_3)
        self.label_v1.setObjectName(u"label_v1")
        sizePolicy.setHeightForWidth(self.label_v1.sizePolicy().hasHeightForWidth())
        self.label_v1.setSizePolicy(sizePolicy)
        self.label_v1.setMinimumSize(QSize(120, 30))
        self.label_v1.setMaximumSize(QSize(200, 30))
        self.label_v1.setFont(font1)
        self.label_v1.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v1, 0, 0, 1, 1)

        self.line_v1 = QLineEdit(self.frame_3)
        self.line_v1.setObjectName(u"line_v1")
        self.line_v1.setEnabled(False)
        self.line_v1.setMinimumSize(QSize(115, 32))
        self.line_v1.setMaximumSize(QSize(400, 32))
        self.line_v1.setFont(font1)
        self.line_v1.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v1, 0, 1, 1, 1)

        self.label_v2 = QLabel(self.frame_3)
        self.label_v2.setObjectName(u"label_v2")
        sizePolicy.setHeightForWidth(self.label_v2.sizePolicy().hasHeightForWidth())
        self.label_v2.setSizePolicy(sizePolicy)
        self.label_v2.setMinimumSize(QSize(120, 30))
        self.label_v2.setMaximumSize(QSize(200, 30))
        self.label_v2.setFont(font1)
        self.label_v2.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v2, 0, 2, 1, 1)

        self.line_v2 = QLineEdit(self.frame_3)
        self.line_v2.setObjectName(u"line_v2")
        self.line_v2.setEnabled(False)
        self.line_v2.setMinimumSize(QSize(115, 32))
        self.line_v2.setMaximumSize(QSize(400, 32))
        self.line_v2.setFont(font1)
        self.line_v2.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v2, 0, 3, 1, 1)

        self.label_v3 = QLabel(self.frame_3)
        self.label_v3.setObjectName(u"label_v3")
        sizePolicy.setHeightForWidth(self.label_v3.sizePolicy().hasHeightForWidth())
        self.label_v3.setSizePolicy(sizePolicy)
        self.label_v3.setMinimumSize(QSize(120, 30))
        self.label_v3.setMaximumSize(QSize(200, 30))
        self.label_v3.setFont(font1)
        self.label_v3.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v3, 0, 4, 1, 1)

        self.line_v3 = QLineEdit(self.frame_3)
        self.line_v3.setObjectName(u"line_v3")
        self.line_v3.setEnabled(False)
        self.line_v3.setMinimumSize(QSize(115, 32))
        self.line_v3.setMaximumSize(QSize(400, 32))
        self.line_v3.setFont(font1)
        self.line_v3.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v3, 0, 5, 1, 1)

        self.label_v4 = QLabel(self.frame_3)
        self.label_v4.setObjectName(u"label_v4")
        sizePolicy.setHeightForWidth(self.label_v4.sizePolicy().hasHeightForWidth())
        self.label_v4.setSizePolicy(sizePolicy)
        self.label_v4.setMinimumSize(QSize(120, 30))
        self.label_v4.setMaximumSize(QSize(200, 30))
        self.label_v4.setFont(font3)
        self.label_v4.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v4, 0, 6, 1, 1)

        self.line_v4 = QLineEdit(self.frame_3)
        self.line_v4.setObjectName(u"line_v4")
        self.line_v4.setEnabled(False)
        self.line_v4.setMinimumSize(QSize(115, 32))
        self.line_v4.setMaximumSize(QSize(400, 32))
        self.line_v4.setFont(font1)
        self.line_v4.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v4, 0, 7, 1, 1)

        self.label_v5 = QLabel(self.frame_3)
        self.label_v5.setObjectName(u"label_v5")
        sizePolicy.setHeightForWidth(self.label_v5.sizePolicy().hasHeightForWidth())
        self.label_v5.setSizePolicy(sizePolicy)
        self.label_v5.setMinimumSize(QSize(120, 30))
        self.label_v5.setMaximumSize(QSize(200, 30))
        self.label_v5.setFont(font1)
        self.label_v5.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v5, 1, 0, 1, 1)

        self.line_v5 = QLineEdit(self.frame_3)
        self.line_v5.setObjectName(u"line_v5")
        self.line_v5.setEnabled(False)
        self.line_v5.setMinimumSize(QSize(115, 32))
        self.line_v5.setMaximumSize(QSize(400, 32))
        self.line_v5.setFont(font1)
        self.line_v5.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v5, 1, 1, 1, 1)

        self.label_v6 = QLabel(self.frame_3)
        self.label_v6.setObjectName(u"label_v6")
        sizePolicy.setHeightForWidth(self.label_v6.sizePolicy().hasHeightForWidth())
        self.label_v6.setSizePolicy(sizePolicy)
        self.label_v6.setMinimumSize(QSize(120, 30))
        self.label_v6.setMaximumSize(QSize(200, 30))
        self.label_v6.setFont(font1)
        self.label_v6.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v6, 1, 2, 1, 1)

        self.line_v6 = QLineEdit(self.frame_3)
        self.line_v6.setObjectName(u"line_v6")
        self.line_v6.setEnabled(False)
        self.line_v6.setMinimumSize(QSize(115, 32))
        self.line_v6.setMaximumSize(QSize(400, 32))
        self.line_v6.setFont(font1)
        self.line_v6.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v6, 1, 3, 1, 1)

        self.label_v7 = QLabel(self.frame_3)
        self.label_v7.setObjectName(u"label_v7")
        sizePolicy.setHeightForWidth(self.label_v7.sizePolicy().hasHeightForWidth())
        self.label_v7.setSizePolicy(sizePolicy)
        self.label_v7.setMinimumSize(QSize(120, 30))
        self.label_v7.setMaximumSize(QSize(200, 30))
        self.label_v7.setFont(font1)
        self.label_v7.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v7, 1, 4, 1, 1)

        self.line_v7 = QLineEdit(self.frame_3)
        self.line_v7.setObjectName(u"line_v7")
        self.line_v7.setEnabled(False)
        self.line_v7.setMinimumSize(QSize(115, 32))
        self.line_v7.setMaximumSize(QSize(400, 32))
        self.line_v7.setFont(font1)
        self.line_v7.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v7, 1, 5, 1, 1)

        self.label_v8 = QLabel(self.frame_3)
        self.label_v8.setObjectName(u"label_v8")
        sizePolicy.setHeightForWidth(self.label_v8.sizePolicy().hasHeightForWidth())
        self.label_v8.setSizePolicy(sizePolicy)
        self.label_v8.setMinimumSize(QSize(120, 30))
        self.label_v8.setMaximumSize(QSize(200, 30))
        self.label_v8.setFont(font3)
        self.label_v8.setStyleSheet(u"color:rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.label_v8, 1, 6, 1, 1)

        self.line_v8 = QLineEdit(self.frame_3)
        self.line_v8.setObjectName(u"line_v8")
        self.line_v8.setEnabled(False)
        self.line_v8.setMinimumSize(QSize(115, 32))
        self.line_v8.setMaximumSize(QSize(400, 32))
        self.line_v8.setFont(font1)
        self.line_v8.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(0,0,50);\n"
"	border-radius:4px;\n"
"	background:rgb(0,0,50);\n"
"}")

        self.gridLayout_3.addWidget(self.line_v8, 1, 7, 1, 1)

        self.visualisation1 = QGraphicsView(self.frame_3)
        self.visualisation1.setObjectName(u"visualisation1")
        self.visualisation1.setMinimumSize(QSize(470, 300))
        self.visualisation1.setMaximumSize(QSize(3000, 3000))

        self.gridLayout_3.addWidget(self.visualisation1, 2, 0, 1, 4)

        self.visualisation2 = QGraphicsView(self.frame_3)
        self.visualisation2.setObjectName(u"visualisation2")
        self.visualisation2.setMinimumSize(QSize(470, 300))
        self.visualisation2.setMaximumSize(QSize(3000, 3000))

        self.gridLayout_3.addWidget(self.visualisation2, 2, 4, 1, 4)

        self.visualisation3 = QGraphicsView(self.frame_3)
        self.visualisation3.setObjectName(u"visualisation3")
        self.visualisation3.setMinimumSize(QSize(470, 300))
        self.visualisation3.setMaximumSize(QSize(3000, 3000))

        self.gridLayout_3.addWidget(self.visualisation3, 3, 0, 1, 4)

        self.visualisation4 = QGraphicsView(self.frame_3)
        self.visualisation4.setObjectName(u"visualisation4")
        self.visualisation4.setMinimumSize(QSize(470, 300))
        self.visualisation4.setMaximumSize(QSize(3000, 3000))

        self.gridLayout_3.addWidget(self.visualisation4, 3, 4, 1, 4)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_android)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font6)
        self.frame_tab.setStyleSheet(u"background:rgb(0,0,50);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font7 = QFont()
        font7.setFamily(u"Segoe UI Light")
        font7.setPointSize(10)
        self.lab_tab.setFont(font7)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(0,0,50);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_bug.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_bug.setText("")
#if QT_CONFIG(tooltip)
        self.bn_cloud.setToolTip(QCoreApplication.translate("MainWindow", u"Cloud", None))
#endif // QT_CONFIG(tooltip)
        self.bn_cloud.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android.setToolTip(QCoreApplication.translate("MainWindow", u"Android", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android.setText("")
        self.label_home_1.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.label_home_4.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.line_home_2.setText(QCoreApplication.translate("MainWindow", u"2021", None))
        self.line_home_3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.line_home_4.setText(QCoreApplication.translate("MainWindow", u"CDR", None))
        self.line_home_1.setText(QCoreApplication.translate("MainWindow", u"BC6000", None))
        self.label_home_2.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_home_3.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Overview</span></p></body></html>", None))
        self.overview_dataset.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.dataname.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.rownumber.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.rownumber.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.rownumber.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.rownumber.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.rownumber.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.rownumber.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.rownumber.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.rownumber.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.rownumber.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.rownumber.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.overview_model.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.modelname.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.overview_predict.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Overview", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.lab_Bug.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p> Analyst</p></body></html>", None))
        self.analyst_traindata.setText(QCoreApplication.translate("MainWindow", u"Train Dataset", None))
        self.analyst_trainname.setItemText(0, QCoreApplication.translate("MainWindow", u"ASP", None))
        self.analyst_trainname.setItemText(1, QCoreApplication.translate("MainWindow", u"HGB", None))
        self.analyst_trainname.setItemText(2, "")
        self.analyst_trainname.setItemText(3, "")
        self.analyst_trainname.setItemText(4, "")

        self.analyst_model.setItemText(0, QCoreApplication.translate("MainWindow", u"OneClassSvm", None))
        self.analyst_model.setItemText(1, QCoreApplication.translate("MainWindow", u"Cluster", None))
        self.analyst_model.setItemText(2, "")
        self.analyst_model.setItemText(3, "")
        self.analyst_model.setItemText(4, "")

        self.analyst_train.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.analyst_save.setText(QCoreApplication.translate("MainWindow", u"Save Model", None))
        self.table_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.table_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Warning", None))
        self.table_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Solved", None))
        self.table_mode.setItemText(2, "")

        self.table_delete.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        ___qtablewidgetitem = self.eventtable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem1 = self.eventtable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.eventtable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.eventtable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.label_v1.setText(QCoreApplication.translate("MainWindow", u"Temp(\u00b0C)", None))
        self.line_v1.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_v2.setText(QCoreApplication.translate("MainWindow", u"Humidty(%rh)", None))
        self.line_v2.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_v3.setText(QCoreApplication.translate("MainWindow", u"Noise(dB)", None))
        self.line_v3.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.label_v4.setText(QCoreApplication.translate("MainWindow", u"PM2.5(\u03bcg/m\u00b3)", None))
        self.line_v4.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.label_v5.setText(QCoreApplication.translate("MainWindow", u"WP(Level)", None))
        self.line_v5.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_v6.setText(QCoreApplication.translate("MainWindow", u"WD(\u00b0)", None))
        self.line_v6.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_v7.setText(QCoreApplication.translate("MainWindow", u"WS(m/s)", None))
        self.line_v7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_v8.setText(QCoreApplication.translate("MainWindow", u"PM10(mg/m\u00b3)", None))
        self.line_v8.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

