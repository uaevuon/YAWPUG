# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionBatch_mode = QAction(MainWindow)
        self.actionBatch_mode.setObjectName(u"actionBatch_mode")
        self.actionBatch_mode.setCheckable(True)
        self.actionSave_config = QAction(MainWindow)
        self.actionSave_config.setObjectName(u"actionSave_config")
        self.actionLoad_config = QAction(MainWindow)
        self.actionLoad_config.setObjectName(u"actionLoad_config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_hbox = QHBoxLayout()
        self.input_hbox.setObjectName(u"input_hbox")
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")

        self.input_hbox.addWidget(self.input_label)

        self.input_path = QLineEdit(self.centralwidget)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setReadOnly(True)

        self.input_hbox.addWidget(self.input_path)

        self.input_select = QPushButton(self.centralwidget)
        self.input_select.setObjectName(u"input_select")

        self.input_hbox.addWidget(self.input_select)


        self.verticalLayout.addLayout(self.input_hbox)

        self.output_hbox = QHBoxLayout()
        self.output_hbox.setObjectName(u"output_hbox")
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")

        self.output_hbox.addWidget(self.output_label)

        self.output_path = QLineEdit(self.centralwidget)
        self.output_path.setObjectName(u"output_path")
        self.output_path.setReadOnly(True)

        self.output_hbox.addWidget(self.output_path)

        self.output_select = QPushButton(self.centralwidget)
        self.output_select.setObjectName(u"output_select")

        self.output_hbox.addWidget(self.output_select)


        self.verticalLayout.addLayout(self.output_hbox)

        self.encode_hbox = QHBoxLayout()
        self.encode_hbox.setObjectName(u"encode_hbox")
        self.lossless_button = QRadioButton(self.centralwidget)
        self.lossless_button.setObjectName(u"lossless_button")
        self.lossless_button.setChecked(True)

        self.encode_hbox.addWidget(self.lossless_button)

        self.lossy_button = QRadioButton(self.centralwidget)
        self.lossy_button.setObjectName(u"lossy_button")

        self.encode_hbox.addWidget(self.lossy_button)

        self.mixed_button = QRadioButton(self.centralwidget)
        self.mixed_button.setObjectName(u"mixed_button")

        self.encode_hbox.addWidget(self.mixed_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.encode_hbox.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.encode_hbox)

        self.quality_hbox = QHBoxLayout()
        self.quality_hbox.setObjectName(u"quality_hbox")
        self.quality_checkbox = QCheckBox(self.centralwidget)
        self.quality_checkbox.setObjectName(u"quality_checkbox")

        self.quality_hbox.addWidget(self.quality_checkbox)

        self.quality_slider = QSlider(self.centralwidget)
        self.quality_slider.setObjectName(u"quality_slider")
        self.quality_slider.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.quality_slider.sizePolicy().hasHeightForWidth())
        self.quality_slider.setSizePolicy(sizePolicy1)
        self.quality_slider.setMaximum(100)
        self.quality_slider.setValue(75)
        self.quality_slider.setOrientation(Qt.Horizontal)

        self.quality_hbox.addWidget(self.quality_slider)

        self.quality_value = QLabel(self.centralwidget)
        self.quality_value.setObjectName(u"quality_value")

        self.quality_hbox.addWidget(self.quality_value)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.quality_hbox.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.quality_hbox)

        self.compression_hbox = QHBoxLayout()
        self.compression_hbox.setObjectName(u"compression_hbox")
        self.compression_checkbox = QCheckBox(self.centralwidget)
        self.compression_checkbox.setObjectName(u"compression_checkbox")

        self.compression_hbox.addWidget(self.compression_checkbox)

        self.compression_slider = QSlider(self.centralwidget)
        self.compression_slider.setObjectName(u"compression_slider")
        self.compression_slider.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.compression_slider.sizePolicy().hasHeightForWidth())
        self.compression_slider.setSizePolicy(sizePolicy1)
        self.compression_slider.setMaximum(6)
        self.compression_slider.setValue(4)
        self.compression_slider.setOrientation(Qt.Horizontal)
        self.compression_slider.setInvertedControls(False)

        self.compression_hbox.addWidget(self.compression_slider)

        self.compression_value = QLabel(self.centralwidget)
        self.compression_value.setObjectName(u"compression_value")

        self.compression_hbox.addWidget(self.compression_value)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.compression_hbox.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.compression_hbox)

        self.min_size_checkbox = QCheckBox(self.centralwidget)
        self.min_size_checkbox.setObjectName(u"min_size_checkbox")
        self.min_size_checkbox.setChecked(False)

        self.verticalLayout.addWidget(self.min_size_checkbox)

        self.metadata_hbox = QHBoxLayout()
        self.metadata_hbox.setObjectName(u"metadata_hbox")
        self.metadata_checkbox = QCheckBox(self.centralwidget)
        self.metadata_checkbox.setObjectName(u"metadata_checkbox")

        self.metadata_hbox.addWidget(self.metadata_checkbox)

        self.metadata_combobox = QComboBox(self.centralwidget)
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.addItem("")
        self.metadata_combobox.setObjectName(u"metadata_combobox")
        self.metadata_combobox.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.metadata_combobox.sizePolicy().hasHeightForWidth())
        self.metadata_combobox.setSizePolicy(sizePolicy1)

        self.metadata_hbox.addWidget(self.metadata_combobox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.metadata_hbox.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.metadata_hbox)

        self.multi_threading = QCheckBox(self.centralwidget)
        self.multi_threading.setObjectName(u"multi_threading")
        self.multi_threading.setChecked(False)

        self.verticalLayout.addWidget(self.multi_threading)

        self.advanced_label = QLabel(self.centralwidget)
        self.advanced_label.setObjectName(u"advanced_label")

        self.verticalLayout.addWidget(self.advanced_label)

        self.temp_kmin = QLabel(self.centralwidget)
        self.temp_kmin.setObjectName(u"temp_kmin")

        self.verticalLayout.addWidget(self.temp_kmin)

        self.filter_hbox = QHBoxLayout()
        self.filter_hbox.setObjectName(u"filter_hbox")
        self.filter_checkbox = QCheckBox(self.centralwidget)
        self.filter_checkbox.setObjectName(u"filter_checkbox")
        self.filter_checkbox.setEnabled(True)

        self.filter_hbox.addWidget(self.filter_checkbox)

        self.filter_slider = QSlider(self.centralwidget)
        self.filter_slider.setObjectName(u"filter_slider")
        self.filter_slider.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.filter_slider.sizePolicy().hasHeightForWidth())
        self.filter_slider.setSizePolicy(sizePolicy1)
        self.filter_slider.setMaximum(100)
        self.filter_slider.setOrientation(Qt.Horizontal)

        self.filter_hbox.addWidget(self.filter_slider)

        self.filter_value = QLabel(self.centralwidget)
        self.filter_value.setObjectName(u"filter_value")

        self.filter_hbox.addWidget(self.filter_value)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filter_hbox.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.filter_hbox)

        self.convert_button = QCommandLinkButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setEnabled(False)

        self.verticalLayout.addWidget(self.convert_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 360, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionBatch_mode)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSave_config)
        self.menuMenu.addAction(self.actionLoad_config)

        self.retranslateUi(MainWindow)
        self.quality_slider.valueChanged.connect(self.quality_value.setNum)
        self.compression_slider.valueChanged.connect(self.compression_value.setNum)
        self.quality_checkbox.clicked["bool"].connect(self.quality_slider.setEnabled)
        self.filter_slider.valueChanged.connect(self.filter_value.setNum)
        self.filter_checkbox.clicked["bool"].connect(self.filter_slider.setEnabled)
        self.compression_checkbox.clicked["bool"].connect(self.compression_slider.setEnabled)
        self.metadata_checkbox.clicked["bool"].connect(self.metadata_combobox.setEnabled)

        self.metadata_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBatch_mode.setText(QCoreApplication.translate("MainWindow", u"Batch mode", None))
        self.actionSave_config.setText(QCoreApplication.translate("MainWindow", u"Save options", None))
        self.actionLoad_config.setText(QCoreApplication.translate("MainWindow", u"Load options", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"input file", None))
        self.input_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"output file", None))
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
        self.quality_value.setText(QCoreApplication.translate("MainWindow", u"75", None))
#if QT_CONFIG(tooltip)
        self.compression_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"compression method (0=fast, 6=slowest)", None))
#endif // QT_CONFIG(tooltip)
        self.compression_checkbox.setText(QCoreApplication.translate("MainWindow", u"compression method", None))
        self.compression_value.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.min_size_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"minimize output size (default:off)", None))
#endif // QT_CONFIG(tooltip)
        self.min_size_checkbox.setText(QCoreApplication.translate("MainWindow", u"minimize size", None))
#if QT_CONFIG(tooltip)
        self.metadata_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"comma separated list of metadata to copy from the input to the output if present (default:xmp)", None))
#endif // QT_CONFIG(tooltip)
        self.metadata_checkbox.setText(QCoreApplication.translate("MainWindow", u"metadata", None))
        self.metadata_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"all", None))
        self.metadata_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"none", None))
        self.metadata_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"icc", None))
        self.metadata_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"xmp", None))

        self.metadata_combobox.setCurrentText(QCoreApplication.translate("MainWindow", u"all", None))
#if QT_CONFIG(tooltip)
        self.multi_threading.setToolTip(QCoreApplication.translate("MainWindow", u"use multi-threading if available", None))
#endif // QT_CONFIG(tooltip)
        self.multi_threading.setText(QCoreApplication.translate("MainWindow", u"multi-threading", None))
        self.advanced_label.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
#if QT_CONFIG(tooltip)
        self.temp_kmin.setToolTip(QCoreApplication.translate("MainWindow", u"min distance between key frames", None))
#endif // QT_CONFIG(tooltip)
        self.temp_kmin.setText(QCoreApplication.translate("MainWindow", u"kmin", None))
        self.filter_checkbox.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.filter_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

