from calc import MyWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    sys.exit(app.exec())

