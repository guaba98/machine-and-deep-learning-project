# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserCell.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 100)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(250, 100))
        self.frame.setStyleSheet("#frame{\n"
"        background-color: rgb(255, 255, 255);\n"
"        border-radius:10px;\n"
"            }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(34, 20, 34, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(166, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(166, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_lab = QtWidgets.QLabel(self.frame_2)
        self.img_lab.setMinimumSize(QtCore.QSize(50, 50))
        self.img_lab.setMaximumSize(QtCore.QSize(50, 50))
        self.img_lab.setStyleSheet("")
        self.img_lab.setObjectName("img_lab")
        self.horizontalLayout_2.addWidget(self.img_lab)
        self.name_lab = QtWidgets.QLabel(self.frame_2)
        self.name_lab.setObjectName("name_lab")
        self.horizontalLayout_2.addWidget(self.name_lab)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.img_lab.setText(_translate("Form", "img"))
        self.name_lab.setText(_translate("Form", "name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
