# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 587)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(2, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lblDisplay = QtWidgets.QLabel(Form)
        self.lblDisplay.setMinimumSize(QtCore.QSize(150, 150))
        self.lblDisplay.setText("")
        self.lblDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDisplay.setObjectName("lblDisplay")
        self.verticalLayout.addWidget(self.lblDisplay)
        self.pbAddImg = QtWidgets.QPushButton(Form)
        self.pbAddImg.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbAddImg.setFont(font)
        self.pbAddImg.setObjectName("pbAddImg")
        self.verticalLayout.addWidget(self.pbAddImg)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(-1, -1, -1, 5)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.leCode = QtWidgets.QLineEdit(Form)
        self.leCode.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.leCode.setFont(font)
        self.leCode.setToolTip("")
        self.leCode.setToolTipDuration(-1)
        self.leCode.setWhatsThis("")
        self.leCode.setText("")
        self.leCode.setMaxLength(10)
        self.leCode.setObjectName("leCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leCode)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lblImgPath = QtWidgets.QLabel(Form)
        self.lblImgPath.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImgPath.sizePolicy().hasHeightForWidth())
        self.lblImgPath.setSizePolicy(sizePolicy)
        self.lblImgPath.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblImgPath.setFont(font)
        self.lblImgPath.setTextFormat(QtCore.Qt.RichText)
        self.lblImgPath.setScaledContents(True)
        self.lblImgPath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblImgPath.setWordWrap(True)
        self.lblImgPath.setObjectName("lblImgPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblImgPath)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.teComment = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teComment.sizePolicy().hasHeightForWidth())
        self.teComment.setSizePolicy(sizePolicy)
        self.teComment.setMinimumSize(QtCore.QSize(0, 40))
        self.teComment.setObjectName("teComment")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.teComment)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(3, 1, 3, 1)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.twProperties = QtWidgets.QTableWidget(self.frame)
        self.twProperties.setFrameShape(QtWidgets.QFrame.Panel)
        self.twProperties.setLineWidth(0)
        self.twProperties.setMidLineWidth(0)
        self.twProperties.setObjectName("twProperties")
        self.twProperties.setColumnCount(0)
        self.twProperties.setRowCount(0)
        self.verticalLayout_2.addWidget(self.twProperties)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(2, 3, 2, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAddProperty = QtWidgets.QPushButton(self.frame)
        self.pbAddProperty.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbAddProperty.setFont(font)
        self.pbAddProperty.setObjectName("pbAddProperty")
        self.horizontalLayout.addWidget(self.pbAddProperty)
        spacerItem = QtWidgets.QSpacerItem(88, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbRemoveProperty = QtWidgets.QPushButton(self.frame)
        self.pbRemoveProperty.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbRemoveProperty.setFont(font)
        self.pbRemoveProperty.setObjectName("pbRemoveProperty")
        self.horizontalLayout.addWidget(self.pbRemoveProperty)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbSave = QtWidgets.QPushButton(Form)
        self.pbSave.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbSave.setFont(font)
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_3.addWidget(self.pbSave)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Image preview:"))
        self.pbAddImg.setText(_translate("Form", "Add..."))
        self.label_2.setText(_translate("Form", "Code:"))
        self.leCode.setPlaceholderText(_translate("Form", "Come up with a name"))
        self.label_3.setText(_translate("Form", "Img path:"))
        self.lblImgPath.setText(_translate("Form", "path to image"))
        self.label_5.setText(_translate("Form", "Comment:"))
        self.label_4.setText(_translate("Form", "Properties:"))
        self.pbAddProperty.setText(_translate("Form", "Add"))
        self.pbRemoveProperty.setText(_translate("Form", "Remove"))
        self.pbSave.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
