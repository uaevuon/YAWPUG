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
        self.options=['']*6
        
        self.setWindowTitle("YAWPUG - Yet Another WebP Utilities Gui")
        self.ui.statusbar.showMessage('Ready')
        
        #basic usage
        self.ui.input_select.clicked.connect(self.input_selector)
        self.ui.output_select.clicked.connect(self.output_selector)
        self.ui.convert_button.clicked.connect(self.convert_clicked)
        
        #options
        self.ui.lossless_button.clicked.connect(self.set_compression)
        self.ui.lossy_button.clicked.connect(self.set_compression)
        self.ui.mixed_button.clicked.connect(self.set_compression)
        self.ui.quality_checkbox.clicked.connect(self.set_quality)
        self.ui.quality_slider.valueChanged.connect(self.set_quality)
        self.ui.min_size_checkbox.clicked.connect(self.set_min_size)

        
    def input_selector(self):
        fname = QFileDialog.getOpenFileName(self,'','','GIF Image(*.gif)')
        self.ui.input_path.setText(fname[0])
        self.ui.output_path.setText('.webp'.join(fname[0].rsplit('.gif', 1))) #Simulate rreplace('.gif', '.webp', 1)
    
    def output_selector(self):
        fname = QFileDialog.getSaveFileName(self,'','','WebP Image(*.webp)')
        self.ui.output_path.setText(fname[0])
        
    def set_compression(self):
        if self.ui.lossless_button.isChecked():
            self.options[0]=''
        if self.ui.lossy_button.isChecked():
            self.options[0]='-lossy'
        if self.ui.mixed_button.isChecked():
            self.options[0]='-mixed'
        self.updateStatusBar()
        
    def set_quality(self):
        self.options[1:3]=['-q', str(self.ui.quality_slider.value())] if self.ui.quality_checkbox.isChecked() else ['','']
        self.updateStatusBar()
        
    def set_min_size(self):
        self.options[3] = '-min_size' if self.ui.min_size_checkbox.isChecked() else ''
        self.updateStatusBar()
                
    def convert_clicked(self):
        self.ui.statusbar.showMessage('Converting...')
        self.ui.statusbar.repaint()
        
        self.args=[self.BIN_PATH]
        self.args.extend(self.options)
        gif_file = self.ui.input_path.text()
        webp_file = self.ui.output_path.text()
        self.args.extend((gif_file, '-o', webp_file))
        
        subprocess.run(self.args, capture_output=True, creationflags = CREATE_NO_WINDOW)
        self.ui.statusbar.showMessage(f'Done. Size comparison: {100*((QFileInfo(webp_file).size()/QFileInfo(gif_file).size())-1):.2f}%')
        
    def updateStatusBar(self): 
        self.ui.statusbar.showMessage('options: ' + ' '.join(self.options))


if __name__ == "__main__":
    app = QApplication.instance()
    if app is None: 
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())