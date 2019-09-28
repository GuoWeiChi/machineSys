# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\code\PRML辅助教学系统\probability.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.pushButtonBia = QtWidgets.QPushButton(Dialog)
        self.pushButtonBia.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButtonBia.setObjectName("pushButtonBia")
        self.pushButtonBeta = QtWidgets.QPushButton(Dialog)
        self.pushButtonBeta.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pushButtonBeta.setObjectName("pushButtonBeta")
        self.pushButtonLogCurve = QtWidgets.QPushButton(Dialog)
        self.pushButtonLogCurve.setGeometry(QtCore.QRect(220, 50, 75, 23))
        self.pushButtonLogCurve.setObjectName("pushButtonLogCurve")
        self.pushButtonAvg = QtWidgets.QPushButton(Dialog)
        self.pushButtonAvg.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.pushButtonAvg.setObjectName("pushButtonAvg")
        self.pushButtonGauss = QtWidgets.QPushButton(Dialog)
        self.pushButtonGauss.setGeometry(QtCore.QRect(20, 100, 91, 23))
        self.pushButtonGauss.setObjectName("pushButtonGauss")
        self.pushButtonEM = QtWidgets.QPushButton(Dialog)
        self.pushButtonEM.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButtonEM.setObjectName("pushButtonEM")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonBia.setText(_translate("Dialog", "二项分布"))
        self.pushButtonBeta.setText(_translate("Dialog", "beta分布"))
        self.pushButtonLogCurve.setText(_translate("Dialog", "log曲线"))
        self.pushButtonAvg.setText(_translate("Dialog", "均匀分布"))
        self.pushButtonGauss.setText(_translate("Dialog", "均匀分布求均值"))
        self.pushButtonEM.setText(_translate("Dialog", "EM模型"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
