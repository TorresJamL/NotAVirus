### Desktop Game? ###
#? Give the player tasks they must do within their browser
#! Create things on the desktop that players must manage outside of their browser
#* If those things are left alone for too long, end the game, and close it out.
import sys 
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowMinMaxButtonsHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set the size of the window to the size of the screen
        self.windowWidth, self.windowHeight = pyautogui.size()
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)
        self.setWindowTitle("Game")

        # Create a central widget and layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)
        self.initUI()

    def initUI(self):
        button = QPushButton("X", self)
        button.setGeometry(0, 0, 50, 50)
        button.setStyleSheet("font-size: 20px; background: lightgray;")
        button.clicked.connect(self.onExitButtonClick)

    def onExitButtonClick(self):
        print("Exit button pressed!")
        self.close()

    def closeEvent(self, event):
        print("closing event called.")
        QApplication.instance().quit()

class LoadingGif(object):
    def __init__(self, gif_name: str):
        self.__gif_name = gif_name
        self.__label = None
        self.__movie = None

    def addGif(self, parent_layout):
        # Create a label for the GIF
        self.__label = QtWidgets.QLabel()
        self.__label.setMinimumSize(QtCore.QSize(250, 250))
        self.__label.setMaximumSize(QtCore.QSize(250, 250))

        # Load and set the GIF
        self.__movie = QMovie(self.__gif_name)
        self.__label.setMovie(self.__movie)

        # Add the label to the parent layout
        parent_layout.addWidget(self.__label)

        # Start the animation
        self.startAnimation()

    def startAnimation(self):
        if self.__movie:
            self.__movie.start()

    def stopAnimation(self):
        if self.__movie:
            self.__movie.stop()

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    demo = LoadingGif("eyeopening.gif")
    demo.addGif(window.layout) 
    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()