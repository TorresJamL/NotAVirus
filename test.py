import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Button
        button = QPushButton("X", self)
        button.setGeometry(100, 100, 50, 50)
        button.setStyleSheet("font-size: 20px; background: lightgray;")
        button.clicked.connect(self.onExitButtonClick)

    def onExitButtonClick(self):
        print("Exit button pressed!")
        self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
