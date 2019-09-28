# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\code\PRML辅助教学系统\linaRegression.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(427, 163)
        Dialog.setMouseTracking(False)
        Dialog.setSizeGripEnabled(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 12, 403, 142))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditNum = QtWidgets.QLineEdit(self.widget)
        self.lineEditNum.setObjectName("lineEditNum")
        self.horizontalLayout.addWidget(self.lineEditNum)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditPower = QtWidgets.QLineEdit(self.widget)
        self.lineEditPower.setObjectName("lineEditPower")
        self.horizontalLayout_2.addWidget(self.lineEditPower)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.isNormal = QtWidgets.QCheckBox(self.widget)
        self.isNormal.setObjectName("isNormal")
        self.horizontalLayout_4.addWidget(self.isNormal)
        self.lambdaInfo = QtWidgets.QLabel(self.widget)
        self.lambdaInfo.setObjectName("lambdaInfo")
        self.horizontalLayout_4.addWidget(self.lambdaInfo)
        self.lineEditLambda = QtWidgets.QLineEdit(self.widget)
        self.lineEditLambda.setEnabled(True)
        self.lineEditLambda.setObjectName("lineEditLambda")
        self.horizontalLayout_4.addWidget(self.lineEditLambda)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButtonStart = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/cartoon4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStart.setIcon(icon)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.verticalLayout.addWidget(self.pushButtonStart)
        self.pushButtonErrStatistic = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/cartoon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonErrStatistic.setIcon(icon1)
        self.pushButtonErrStatistic.setObjectName("pushButtonErrStatistic")
        self.verticalLayout.addWidget(self.pushButtonErrStatistic)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "多项式拟合"))
        self.label_3.setText(_translate("Dialog", "要生成的测试数据的数量:"))
        self.lineEditNum.setText(_translate("Dialog", "30"))
        self.label_4.setText(_translate("Dialog", "范围:[1-100]的整数"))
        self.label.setText(_translate("Dialog", "进行拟合的多项式系数:  "))
        self.lineEditPower.setText(_translate("Dialog", "5"))
        self.label_2.setText(_translate("Dialog", " 范围:[0-15]的整数 "))
        self.isNormal.setText(_translate("Dialog", "使用正则化"))
        self.lambdaInfo.setText(_translate("Dialog", "      正则化系数:"))
        self.lineEditLambda.setText(_translate("Dialog", "0.003"))
        self.pushButtonStart.setText(_translate("Dialog", "执行"))
        self.pushButtonErrStatistic.setText(_translate("Dialog", "查看不同多项式拟合的错误率"))
import pics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
