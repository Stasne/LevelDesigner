import sys
import design
import resources
import ResourceManager
import copy
from PyQt5.QtWidgets import *#QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QBrush
from PyQt5.QtCore import *

ItemStyle_selected = "border: 2px solid white;"
ItemStyle_normal = "border: 0px;"

class LevelItem(QLabel):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

    # def enterEvent(self, event):
    #     self.setStyleSheet(ItemStyle_selected)
    #     print("enter event")
    #     return super(LevelItem, self).enterEvent(event)

    # def leaveEvent(self, event):      
    #     self.setStyleSheet(ItemStyle_normal)
    #     print("leave event")
    #     return super(LevelItem, self).enterEvent(event)

    # def mouseReleaseEvent(self, event):  
    #     posMouse =  event.pos()
    #     print("mouse release event")
    #     if self.rect().contains(posMouse):
    #         print ("Under Mouse")
    #     return super(LevelItem, self).mouseReleaseEvent(event)

class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setupUi(self)
        self.setWindowTitle('Level Designer')
        self.createEditor(15, 30)
        self.resourcer = ResourceManager.Resourcer()
        self.actionCreate_resource.triggered.connect(lambda: self.resourcer.show())
        self.actionEdit_resource.triggered.connect(lambda: self.resourcer.editor())
        self.actionExitBut.triggered.connect(lambda: QApplication.closeAllWindows() )
        self.brush = self.makeLevelItem(":/Resources/WL.png")

    def createEditor(self, rows, cols):
        self.twMain.setColumnCount(cols)
        self.twMain.setRowCount(rows)
        for j in range(self.twMain.rowCount()):
            for k in range(self.twMain.columnCount()):
                item = self.makeLevelItem(":/Resources/__.png")
                self.twMain.setCellWidget(j, k, item)

        self.twMain.verticalHeader().hide()
        self.twMain.horizontalHeader().hide()
        self.twMain.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.twMain.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #signals
        self.twMain.itemSelectionChanged.connect(self.onSelection)
        # self.twMain.itemEntered.connect(self.onSelection)
        # self.twMain.cellEntered.connect(self.onCellEntered)
        # self.twMain.cellActivated.connect(self.onCellActivated)
        self.twMain.cellPressed.connect(self.onCellPressed)

    def makeLevelItem(self, image):
        lbl = LevelItem()
        lbl.setScaledContents(True)
        pixmap = QPixmap(image)
        lbl.setPixmap(pixmap)
        return lbl

    def onCellEntered(self, row, col):
        item = self.twMain.item(row, col)
        item = type(self.brush)()
        self.twMain.setCellWidget(row,col, item)
        # print ("table: Cell entered row: " + str(row) + " col: " + str(col))
    
    def onCellActivated(self, row, col): #doubleclick
        print ("table: Cell activated row: " + str(row) + " col: " + str(col))    

    def onCellPressed (self, row, col):
        print ("table: Cell presed row: " + str(row) + " col: " + str(col))        
    def onSelection(self):
        print("table: selection changed")
        # print(len(self.twMain.selectedItems()))
        print(len(self.twMain.selectedRanges()))


    
    def closeEvent(self, event):
        QApplication.closeAllWindows() 


def main():
    
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
