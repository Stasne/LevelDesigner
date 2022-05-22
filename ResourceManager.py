import sys
import json
import resourcer_design
from os import getcwd
from os.path import exists
from PyQt5.QtWidgets import *#QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Resourcer(QWidget, resourcer_design.Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.resource_img = str("")
		self.resources_dir = "Resources"
		self.resource_ext = ".resource"
		self.resource_dest_path = ""
		self.pbAddImg.clicked.connect(self.onAddImageButton)
		self.pbSave.clicked.connect(self.onSave)
		self.leCode.textChanged.connect(lambda: self.checkInput())
		self.pbSave.setEnabled(False)

	def updateImage(self):
		pixmap = QPixmap(self.resource_img)
		self.lblDisplay.setPixmap(pixmap)

	def onAddImageButton(self):
		dlg = QFileDialog()
		dlg.setFileMode(QFileDialog.ExistingFile)
		dlg.setNameFilters(["Text files (*.txt)", "Images (*.png *.jpg)"])
		dlg.selectNameFilter("Images (*.png *.jpg)")
		if dlg.exec_():
			self.resource_img = dlg.selectedFiles()[0]
			self.lblImgPath.setText(self.resource_img)
			self.updateImage()

	def onSave(self):
		if (not self.checkInput()):
			QMessageBox.critical(self, 'CRITICAL ERROR', 'Something wrong with provided data')
			return False

		file_exists = exists(self.resource_dest_path)
		if (file_exists):
			res = QMessageBox.question(self,'File exists',"File '" + self.resource_dest_path +"' exists, rewrite?")
			if (res != QMessageBox.Yes):
				return False
		self.resource_code = self.leCode.text()
		self.resource_comment = self.teComment.toPlainText()
		self.exportResource()

	def checkInput(self):
		if (not self.resource_img):
			return False
		if (not self.leCode.text()):
			return False
		resource_code = self.leCode.text()
		if (not resource_code):
			return False
		self.resource_dest_path = getcwd() + '/'+ self.resources_dir +'/' + resource_code + self.resource_ext
		self.pbSave.setEnabled(True)
		return True

	def exportResource(self):
		print ("Export resource")
		self.toJson()
		QMessageBox.information(self, 'Success', 'Success \nResource saved to:' + self.resource_dest_path)

	def editor(self):
		print("Edit resource")
		dlg = QFileDialog()
		dlg.setFileMode(QFileDialog.ExistingFile)
		filters = "Resources (*" + self.resource_ext + ")"
		dlg.setNameFilters([filters])
		dlg.selectNameFilter(filters)
		if (not dlg.exec_()):
			return False
		
		self.resource_dest_path = dlg.selectedFiles()[0]
		self.importResource(self.resource_dest_path)
		self.leCode.setEnabled(False)
		self.show()

	def toJson(self):
		if (not self.checkInput()):
			QMessageBox.critical(self, 'CRITICAL ERROR', 'Something wrong with provided data')

		properties = dict()
		meAsDict = dict()
		dictionary ={
			"type" : "resource",
		    "code" : self.resource_code,
		    "img" : self.resource_img,
		    "comment" : self.resource_comment
			}
		# Serializing json 
		# return json_object = json.dumps(dictionary, indent = 4)

		json_object = json.dumps(dictionary, indent = 4)
		# Writing to sample.json
		# out_file = self.resource_code + self.resource_ext
		with open(self.resource_dest_path, "w") as outfile:
			outfile.write(json_object)

	def importResource(self, resource_path):
		print("Import resource: " + resource_path)

	def closeEvent(self, event):
		if (self.checkInput()):
			res = QMessageBox.question(self,'R u sure?',"Cancel changes?")
			if (res != QMessageBox.Yes):
				return event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Resourcer()
    view.show()
    sys.exit(app.exec_())