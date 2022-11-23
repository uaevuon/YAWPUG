# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(312, 388)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.input_path = QLineEdit(self.centralwidget)
        self.input_path.setObjectName(u"input_path")

        self.horizontalLayout.addWidget(self.input_path)

        self.input_select = QPushButton(self.centralwidget)
        self.input_select.setObjectName(u"input_select")

        self.horizontalLayout.addWidget(self.input_select)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.output_path = QLineEdit(self.centralwidget)
        self.output_path.setObjectName(u"output_path")

        self.horizontalLayout_2.addWidget(self.output_path)

        self.output_select = QPushButton(self.centralwidget)
        self.output_select.setObjectName(u"output_select")

        self.horizontalLayout_2.addWidget(self.output_select)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(75)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider)


        self.formLayout.setLayout(3, QFormLayout.LabelRole, self.horizontalLayout_4)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.checkBox_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_5.addWidget(self.checkBox_5)

        self.horizontalSlider_2 = QSlider(self.centralwidget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(6)
        self.horizontalSlider_2.setValue(4)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setInvertedControls(False)

        self.horizontalLayout_5.addWidget(self.horizontalSlider_2)


        self.formLayout.setLayout(5, QFormLayout.LabelRole, self.horizontalLayout_5)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_6.addWidget(self.checkBox_3)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.formLayout.setLayout(7, QFormLayout.LabelRole, self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_7.addWidget(self.checkBox_6)

        self.horizontalSlider_3 = QSlider(self.centralwidget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_3)


        self.formLayout.setLayout(8, QFormLayout.LabelRole, self.horizontalLayout_7)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.checkBox)

        self.convert_button = QCommandLinkButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.convert_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 312, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"input_file", None))
        self.input_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"output_file", None))
        self.output_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"loseless", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"lossy", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"mixed", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"quality", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"min_size", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"compression method", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"kmin", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"metadata", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"all", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"none", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"icc", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"xmp", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"all", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"multi-threading", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

