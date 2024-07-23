from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation

class MyButtonWidget(QWidget):

# public
    MyButtonWidget(QWidget parent = None)

def __init__(self, QWidget(parent):

    button = QPushButton(tr("Animated Button"), self)
    anim = QPropertyAnimation(button, "pos", self)
    anim.setDuration(10000)
    anim.setStartValue(QPoint(0, 0))
    anim.setEndValue(QPoint(100, 250))
    anim.start()

if __name__ == "__main__":

    a = QApplication(argc, argv)
    buttonAnimWidget = MyButtonWidget()
    buttonAnimWidget.resize(QSize(800, 600))
    buttonAnimWidget.show()
    return a.exec()