import sys
import subprocess
from subprocess import CREATE_NO_WINDOW
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from PySide6.QtCore import QFile
from ui_mainwidget import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.args=[]
        self.args.append('.\\bin\\gif2webp')
        
        self.setWindowTitle("YAWPUG - Yet Another WebP Utilities Gui")
    
        self.ui.input_select.clicked.connect(self.input_selector)
        self.ui.output_select.clicked.connect(self.output_selector)
        self.ui.convert_button.clicked.connect(self.convert_clicked)

        
    def input_selector(self):
        fname = QFileDialog.getOpenFileName(self,'','','GIF Image(*.gif)')
        self.ui.input_path.setText(fname[0])
        self.ui.output_path.setText('.webp'.join(fname[0].rsplit('.gif', 1))) #Simulate rreplace('.gif', '.webp', 1)
    
    def output_selector(self):
        fname = QFileDialog.getSaveFileName(self,'','','WebP Image(*.webp)')
        self.ui.output_path.setText(fname[0])
        
    def convert_clicked(self):
        gif_file = self.ui.input_path.text()
        webp_file = self.ui.output_path.text()
        self.args.extend((gif_file, '-o', webp_file))
        p=subprocess.run(self.args, capture_output=True, creationflags = CREATE_NO_WINDOW)
        print(p.stdout.decode('utf-8'))


if __name__ == "__main__":
    app = QApplication.instance()
    if app is None: 
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())