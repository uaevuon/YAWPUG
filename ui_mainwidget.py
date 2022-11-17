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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(288, 359)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.input_path = QLineEdit(Form)
        self.input_path.setObjectName(u"input_path")

        self.horizontalLayout.addWidget(self.input_path)

        self.input_select = QPushButton(Form)
        self.input_select.setObjectName(u"input_select")

        self.horizontalLayout.addWidget(self.input_select)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.output_path = QLineEdit(Form)
        self.output_path.setObjectName(u"output_path")

        self.horizontalLayout_2.addWidget(self.output_path)

        self.output_select = QPushButton(Form)
        self.output_select.setObjectName(u"output_select")

        self.horizontalLayout_2.addWidget(self.output_select)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(75)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_5.addWidget(self.checkBox_5)

        self.horizontalSlider_2 = QSlider(Form)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(6)
        self.horizontalSlider_2.setValue(4)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setInvertedControls(False)

        self.horizontalLayout_5.addWidget(self.horizontalSlider_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_6.addWidget(self.checkBox_3)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_7.addWidget(self.checkBox_6)

        self.horizontalSlider_3 = QSlider(Form)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.convert_button = QCommandLinkButton(Form)
        self.convert_button.setObjectName(u"convert_button")

        self.verticalLayout.addWidget(self.convert_button)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"input_file", None))
        self.input_select.setText(QCoreApplication.translate("Form", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"output_file", None))
        self.output_select.setText(QCoreApplication.translate("Form", u"Select", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"loseless", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"lossy", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"mixed", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"quality", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"min_size", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"compression method", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"kmin", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"metadata", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"all", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"none", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"icc", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"xmp", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"all", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"filter", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"multi-threading", None))
        self.convert_button.setText(QCoreApplication.translate("Form", u"Convert", None))
    # retranslateUi

