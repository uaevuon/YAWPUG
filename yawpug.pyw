import sys
import subprocess
from subprocess import CREATE_NO_WINDOW
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from PySide6.QtCore import QFileInfo
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.BIN_PATH='.\\bin\\gif2webp'
        self.options=['']*14
        
        self.setWindowTitle("YAWPUG - Yet Another WebP Utilities Gui")
        self.setFixedSize(390, 410)
        self.ui.statusbar.showMessage('Ready')
        
        # basic usage
        self.ui.input_select.clicked.connect(self.input_selector)
        self.ui.output_select.clicked.connect(self.output_selector)
        self.ui.convert_button.clicked.connect(self.convert_clicked)
        
        # options
        self.ui.lossless_button.clicked.connect(self.set_compression)
        self.ui.lossy_button.clicked.connect(self.set_compression)
        self.ui.mixed_button.clicked.connect(self.set_compression)
        self.ui.quality_checkbox.clicked.connect(self.set_quality)
        self.ui.quality_slider.valueChanged.connect(self.set_quality)
        self.ui.compression_method_checkbox.clicked.connect(self.set_compression_method)
        self.ui.compression_method_slider.valueChanged.connect(self.set_compression_method)
        self.ui.min_size_checkbox.clicked.connect(self.set_min_size)
        self.ui.multi_threading.clicked.connect(self.set_multi_threading)
        
        # advanced options
        self.ui.actionAdvanced_options.triggered.connect(self.set_kmin_kmax)
        self.ui.actionAdvanced_options.triggered.connect(self.set_metadata)
        self.ui.actionAdvanced_options.triggered.connect(self.set_filter)
        self.ui.kmin_kmax_checkbox.clicked.connect(self.set_kmin_kmax)
        self.ui.kmin_spinbox.valueChanged.connect(self.set_kmin_kmax)
        self.ui.kmax_spinbox.valueChanged.connect(self.set_kmin_kmax)
        self.ui.metadata_checkbox.clicked.connect(self.set_metadata)
        self.ui.metadata_combobox.currentTextChanged.connect(self.set_metadata)
        self.ui.filter_checkbox.clicked.connect(self.set_filter)
        self.ui.filter_slider.valueChanged.connect(self.set_filter)

        
    def input_selector(self):
        fname = QFileDialog.getOpenFileName(self,'','','GIF Image(*.gif)')
        self.ui.input_path.setText(fname[0])
        self.ui.output_path.setText('.webp'.join(fname[0].rsplit('.gif', 1))) # Simulate rreplace('.gif', '.webp', 1)
    
    def output_selector(self):
        fname = QFileDialog.getSaveFileName(self,'','','WebP Image(*.webp)')
        self.ui.output_path.setText(fname[0])
        
        
    def set_compression(self):
        if self.ui.lossless_button.isChecked():
            self.options[0] = ''
        if self.ui.lossy_button.isChecked():
            self.options[0] = '-lossy'
        if self.ui.mixed_button.isChecked():
            self.options[0] = '-mixed'
        self.updateStatusBar()
        
    def set_quality(self):
        self.options[1:3] = ['-q', str(self.ui.quality_slider.value())] if self.ui.quality_checkbox.isChecked() else ['','']
        self.updateStatusBar()
        
    def set_compression_method(self):
        self.options[3:5] = ['-m', str(self.ui.compression_method_slider.value())] if self.ui.compression_method_checkbox.isChecked() else ['','']
        self.updateStatusBar()

    def set_min_size(self):
        self.options[5] = '-min_size' if self.ui.min_size_checkbox.isChecked() else ''
        self.updateStatusBar()
        
    def set_multi_threading(self):
        self.options[6] = '-mt' if self.ui.multi_threading.isChecked() else ''
        self.updateStatusBar()
        
    def set_kmin_kmax(self):
        self.options[7:11] = ['-kmin', str(self.ui.kmin_spinbox.value()), '-kmax', str(self.ui.kmax_spinbox.value())] if self.ui.actionAdvanced_options.isChecked() and self.ui.kmin_kmax_checkbox.isChecked() else ['','','','']
        self.updateStatusBar()
        
    def set_metadata(self):
        self.options[11:13] = ['-metadata', self.ui.metadata_combobox.currentText()] if self.ui.actionAdvanced_options.isChecked() and self.ui.metadata_checkbox.isChecked() else ['','']
        self.updateStatusBar()
        
    def set_filter(self):
        self.options[13:15] = ['-f', str(self.ui.filter_slider.value())] if self.ui.actionAdvanced_options.isChecked() and self.ui.filter_checkbox.isChecked() else ['','']
        self.updateStatusBar()

        
    def convert_clicked(self):
        if not (self.ui.input_path.text() and self.ui.output_path.text()):
            self.ui.statusbar.showMessage('Please select input file output files before converting.')
            return
        
        self.ui.statusbar.showMessage('Converting...')
        self.ui.statusbar.repaint()
        
        self.args=[self.BIN_PATH]
        self.args.extend(self.options)
        gif_file = self.ui.input_path.text()
        webp_file = self.ui.output_path.text()
        self.args.extend((gif_file, '-o', webp_file))
        
        subprocess.run(self.args, capture_output=True, creationflags = CREATE_NO_WINDOW)
        self.ui.statusbar.showMessage(f'Done. Size comparison: {100*((QFileInfo(webp_file).size()/QFileInfo(gif_file).size())-1):.1f}%')
        
    def updateStatusBar(self):
        self.ui.statusbar.showMessage('options: ' + ' '.join(i for i in self.options if i)) # Skip empty values



if __name__ == "__main__":
    app = QApplication.instance()
    if app is None: 
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())