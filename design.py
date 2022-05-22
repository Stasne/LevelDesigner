# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 782)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.twMain = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.twMain.sizePolicy().hasHeightForWidth())
        self.twMain.setSizePolicy(sizePolicy)
        self.twMain.setMinimumSize(QtCore.QSize(1025, 525))
        self.twMain.setSizeIncrement(QtCore.QSize(2, 1))
        self.twMain.setBaseSize(QtCore.QSize(0, 0))
        self.twMain.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twMain.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twMain.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.twMain.setAutoScroll(False)
        self.twMain.setProperty("showDropIndicator", False)
        self.twMain.setIconSize(QtCore.QSize(35, 35))
        self.twMain.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.twMain.setGridStyle(QtCore.Qt.DotLine)
        self.twMain.setWordWrap(False)
        self.twMain.setCornerButtonEnabled(False)
        self.twMain.setObjectName("twMain")
        self.twMain.setColumnCount(0)
        self.twMain.setRowCount(0)
        self.verticalLayout_3.addWidget(self.twMain)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.twTools = QtWidgets.QTableWidget(self.frame)
        self.twTools.setObjectName("twTools")
        self.twTools.setColumnCount(0)
        self.twTools.setRowCount(0)
        self.verticalLayout_2.addWidget(self.twTools)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.twProperties = QtWidgets.QTableWidget(self.frame)
        self.twProperties.setObjectName("twProperties")
        self.twProperties.setColumnCount(0)
        self.twProperties.setRowCount(0)
        self.verticalLayout.addWidget(self.twProperties)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1161, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Tools:"))
        self.label.setText(_translate("MainWindow", "Properties:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
