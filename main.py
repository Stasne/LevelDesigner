import sys
import design
import resources
from PyQt5.QtWidgets import *#QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QBrush
from PyQt5.QtCore import *
ItemStyle_selected = "border: 2px solid white;"
ItemStyle_normal = "border: 0px;"
class LevelItem(QLabel):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

    def mouseEvent(self, event):
        print("mouse")
        return super(LevelItem, self).mouseEvent(event)
    def enterEvent(self, event):
        # print ("Mouse Entered")
        # setting up border
        self.setStyleSheet(ItemStyle_selected)
        return super(LevelItem, self).enterEvent(event)

    def leaveEvent(self, event):      
        # print ("Mouse Left")
        self.setStyleSheet(ItemStyle_normal)
        return super(LevelItem, self).enterEvent(event)

    def mouseReleaseEvent(self, event):  
        posMouse =  event.pos()
        if self.rect().contains(posMouse):
            print ("Under Mouse")
        return super(LevelItem, self).mouseReleaseEvent(event)

class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Level Designer')
        self.createEditor()
        
    def createEditor(self):
        self.twMain.setColumnCount(30)
        self.twMain.setRowCount(15)
        for j in range(self.twMain.rowCount()):
            for k in range(self.twMain.columnCount()):
                # self.twMain.setItemDelegateForColumn(k, delegate)
                # brush = QBrush(QPixmap(":/Resources/__.png"))
                # brush = QBrush(QPixmap(":/Resources/WL.png").scaled(36, 36, Qt.KeepAspectRatio, Qt.FastTransformation ))
                # pixmap = QPixmap(":/Resources/WL.png")#.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.FastTransformation )
                item = self.makeLevelItem(":/Resources/WL.png")
                self.twMain.setCellWidget(j, k, item)

        self.twMain.verticalHeader().hide()
        self.twMain.horizontalHeader().hide()
        # self.twMain.verticalHeader().setDefaultSectionSize(35)
        # self.twMain.horizontalHeader().setDefaultSectionSize(35)

        self.twMain.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.twMain.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #signals
        self.twMain.itemSelectionChanged.connect(self.onSelection)

    def makeLevelItem(self, image):
        lbl = LevelItem()
        lbl.setScaledContents(True)
        pixmap = QPixmap(image)
        lbl.setPixmap(pixmap)
        return lbl

    def onSelection(self):
        print(len(self.twMain.selectedItems()))
        # self.setStyleSheet(ItemStyle_selected)
    


def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
