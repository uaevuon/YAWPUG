import subprocess
from subprocess import CREATE_NO_WINDOW
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout


class YAWPUG(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YAWPUG - Yet Another WebP Utilities Gui")
        self.setFixedSize(QSize(700, 400))   
        layout=QHBoxLayout()
        self.setLayout(layout)
        
        self.args=[]
        self.args.append('.\\bin\\gif2webp')

        self.input = QLabel('gif file name')
        layout.addWidget(self.input)
        self.input_path = QLineEdit()
        layout.addWidget(self.input_path)
        
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.Convert_Clicked)
        layout.addWidget(self.convert_button)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
           
    def Convert_Clicked(self):
        gif_file = self.input_path.text()
        webp_file = '.webp'.join(self.input_path.text().rsplit('.gif', 1)) #Simulate rreplace('.gif', '.webp', 1)
        self.args.extend((gif_file, '-o', webp_file))
        p=subprocess.run(self.args, capture_output=True, creationflags = CREATE_NO_WINDOW)
        print(p.stdout.decode('utf-8'))


if __name__ == '__main__':
    app = QApplication.instance()
    if app == None:
        app = QApplication()

    window = YAWPUG()
    window.show()

    app.exec()