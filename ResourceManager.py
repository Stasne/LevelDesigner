import sys
from PyQt5.QtWidgets import *#QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Resourcer(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(600,400)
		self.layout = QHBoxLayout()
		item = QLabel("Dsdsd")
		self.itemName   = QLineEdit(item)
		self.itemName.setReadOnly(True)

		self.itemCount  = QLineEdit()
		self.itemCount.setText("0")
		self.itemCount.setMaximumWidth(40)

		self.decrease   = QPushButton("-")
		self.increase   = QPushButton("+")

		self.layout.addWidget(self.itemName)
		self.layout.addWidget(self.itemCount)
		self.layout.addWidget(self.decrease)
		self.layout.addWidget(self.increase)

		self.setLayout(self.layout)

		


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Resourcer()
    view.show()
    sys.exit(app.exec_())