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
        MainWindow.resize(309, 422)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.input_path = QLineEdit(self.centralwidget)
        self.input_path.setObjectName(u"input_path")

        self.horizontalLayout_7.addWidget(self.input_path)

        self.input_select = QPushButton(self.centralwidget)
        self.input_select.setObjectName(u"input_select")

        self.horizontalLayout_7.addWidget(self.input_select)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.output_path = QLineEdit(self.centralwidget)
        self.output_path.setObjectName(u"output_path")

        self.horizontalLayout_6.addWidget(self.output_path)

        self.output_select = QPushButton(self.centralwidget)
        self.output_select.setObjectName(u"output_select")

        self.horizontalLayout_6.addWidget(self.output_select)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lossless_button = QRadioButton(self.centralwidget)
        self.lossless_button.setObjectName(u"lossless_button")
        self.lossless_button.setChecked(True)

        self.horizontalLayout_5.addWidget(self.lossless_button)

        self.lossy_button = QRadioButton(self.centralwidget)
        self.lossy_button.setObjectName(u"lossy_button")

        self.horizontalLayout_5.addWidget(self.lossy_button)

        self.mixed_button = QRadioButton(self.centralwidget)
        self.mixed_button.setObjectName(u"mixed_button")

        self.horizontalLayout_5.addWidget(self.mixed_button)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.quality_checkbox = QCheckBox(self.centralwidget)
        self.quality_checkbox.setObjectName(u"quality_checkbox")

        self.horizontalLayout_4.addWidget(self.quality_checkbox)

        self.quality_slider = QSlider(self.centralwidget)
        self.quality_slider.setObjectName(u"quality_slider")
        self.quality_slider.setEnabled(False)
        self.quality_slider.setMaximum(100)
        self.quality_slider.setValue(75)
        self.quality_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.quality_slider)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.formLayout.setLayout(3, QFormLayout.LabelRole, self.horizontalLayout_4)

        self.min_size_checkbox = QCheckBox(self.centralwidget)
        self.min_size_checkbox.setObjectName(u"min_size_checkbox")
        self.min_size_checkbox.setChecked(False)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.min_size_checkbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.compression_checkbox = QCheckBox(self.centralwidget)
        self.compression_checkbox.setObjectName(u"compression_checkbox")

        self.horizontalLayout_3.addWidget(self.compression_checkbox)

        self.compression_slider = QSlider(self.centralwidget)
        self.compression_slider.setObjectName(u"compression_slider")
        self.compression_slider.setEnabled(False)
        self.compression_slider.setMaximum(6)
        self.compression_slider.setValue(4)
        self.compression_slider.setOrientation(Qt.Horizontal)
        self.compression_slider.setInvertedControls(False)

        self.horizontalLayout_3.addWidget(self.compression_slider)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.formLayout.setLayout(4, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.metadata_checkbox = QCheckBox(self.centralwidget)
        self.metadata_checkbox.setObjectName(u"metadata_checkbox")

        self.horizontalLayout_2.addWidget(self.metadata_checkbox)

        self.metadata_combobox = QComboBox(self.centralwidget)
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.setObjectName(u"metadata_combobox")
        self.metadata_combobox.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.metadata_combobox)


        self.formLayout.setLayout(6, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_checkbox = QCheckBox(self.centralwidget)
        self.filter_checkbox.setObjectName(u"filter_checkbox")
        self.filter_checkbox.setEnabled(True)

        self.horizontalLayout.addWidget(self.filter_checkbox)

        self.filter_slider = QSlider(self.centralwidget)
        self.filter_slider.setObjectName(u"filter_slider")
        self.filter_slider.setEnabled(False)
        self.filter_slider.setMaximum(100)
        self.filter_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.filter_slider)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)


        self.formLayout.setLayout(10, QFormLayout.LabelRole, self.horizontalLayout)

        self.convert_button = QCommandLinkButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.convert_button)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_5)

        self.multi_threading = QCheckBox(self.centralwidget)
        self.multi_threading.setObjectName(u"multi_threading")
        self.multi_threading.setChecked(False)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.multi_threading)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 309, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quality_slider.valueChanged.connect(self.label.setNum)
        self.compression_slider.valueChanged.connect(self.label_4.setNum)
        self.quality_checkbox.clicked["bool"].connect(self.quality_slider.setEnabled)
        self.filter_slider.valueChanged.connect(self.label_6.setNum)
        self.filter_checkbox.clicked["bool"].connect(self.filter_slider.setEnabled)
        self.compression_checkbox.clicked["bool"].connect(self.compression_slider.setEnabled)
        self.metadata_checkbox.clicked["bool"].connect(self.metadata_combobox.setEnabled)

        self.metadata_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"input_file", None))
        self.input_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"output_file", None))
        self.output_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
#if QT_CONFIG(tooltip)
        self.lossless_button.setToolTip(QCoreApplication.translate("MainWindow", u"encode image using lossless compression.", None))
#endif // QT_CONFIG(tooltip)
        self.lossless_button.setText(QCoreApplication.translate("MainWindow", u"loseless", None))
#if QT_CONFIG(tooltip)
        self.lossy_button.setToolTip(QCoreApplication.translate("MainWindow", u"encode image using lossy compression.", None))
#endif // QT_CONFIG(tooltip)
        self.lossy_button.setText(QCoreApplication.translate("MainWindow", u"lossy", None))
#if QT_CONFIG(tooltip)
        self.mixed_button.setToolTip(QCoreApplication.translate("MainWindow", u"for each frame in the image, pick lossy or lossless compression heuristically.", None))
#endif // QT_CONFIG(tooltip)
        self.mixed_button.setText(QCoreApplication.translate("MainWindow", u"mixed", None))
#if QT_CONFIG(tooltip)
        self.quality_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"quality factor (0:small..100:big)", None))
#endif // QT_CONFIG(tooltip)
        self.quality_checkbox.setText(QCoreApplication.translate("MainWindow", u"quality", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"75", None))
#if QT_CONFIG(tooltip)
        self.min_size_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"minimize output size (default:off)", None))
#endif // QT_CONFIG(tooltip)
        self.min_size_checkbox.setText(QCoreApplication.translate("MainWindow", u"minimize size", None))
#if QT_CONFIG(tooltip)
        self.compression_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"compression method (0=fast, 6=slowest)", None))
#endif // QT_CONFIG(tooltip)
        self.compression_checkbox.setText(QCoreApplication.translate("MainWindow", u"compression method", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.metadata_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"comma separated list of metadata to copy from the input to the output if present (default:xmp)", None))
#endif // QT_CONFIG(tooltip)
        self.metadata_checkbox.setText(QCoreApplication.translate("MainWindow", u"metadata", None))
        self.metadata_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"all", None))
        self.metadata_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"none", None))
        self.metadata_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"icc", None))
        self.metadata_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"xmp", None))

        self.metadata_combobox.setCurrentText(QCoreApplication.translate("MainWindow", u"all", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.filter_checkbox.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"min distance between key frames", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"kmin", None))
#if QT_CONFIG(tooltip)
        self.multi_threading.setToolTip(QCoreApplication.translate("MainWindow", u"use multi-threading if available", None))
#endif // QT_CONFIG(tooltip)
        self.multi_threading.setText(QCoreApplication.translate("MainWindow", u"multi-threading", None))
    # retranslateUi

