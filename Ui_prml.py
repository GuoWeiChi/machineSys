# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\code\PRML辅助教学系统\prml.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 734)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 810, 276))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(190, 190))
        self.label.setMaximumSize(QtCore.QSize(190, 190))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButtonMul = QtWidgets.QPushButton(self.tab)
        self.pushButtonMul.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButtonMul.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/cartoon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMul.setIcon(icon)
        self.pushButtonMul.setObjectName("pushButtonMul")
        self.verticalLayout.addWidget(self.pushButtonMul)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(190, 190))
        self.label_2.setMaximumSize(QtCore.QSize(190, 190))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButtonLine = QtWidgets.QPushButton(self.tab)
        self.pushButtonLine.setMinimumSize(QtCore.QSize(0, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/cartoon1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLine.setIcon(icon1)
        self.pushButtonLine.setObjectName("pushButtonLine")
        self.verticalLayout_2.addWidget(self.pushButtonLine)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(190, 190))
        self.label_3.setMaximumSize(QtCore.QSize(190, 190))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/images/3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.pushButtonLine_bayes = QtWidgets.QPushButton(self.tab)
        self.pushButtonLine_bayes.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonLine_bayes.setIcon(icon1)
        self.pushButtonLine_bayes.setObjectName("pushButtonLine_bayes")
        self.verticalLayout_3.addWidget(self.pushButtonLine_bayes)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMinimumSize(QtCore.QSize(190, 190))
        self.label_4.setMaximumSize(QtCore.QSize(190, 190))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.pushButton_probability = QtWidgets.QPushButton(self.tab)
        self.pushButton_probability.setMaximumSize(QtCore.QSize(190, 30))
        self.pushButton_probability.setIcon(icon1)
        self.pushButton_probability.setObjectName("pushButton_probability")
        self.verticalLayout_4.addWidget(self.pushButton_probability)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, icon1, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonMul.setText(_translate("MainWindow", "产生测试数据"))
        self.pushButtonLine.setText(_translate("MainWindow", "多项式拟合"))
        self.pushButtonLine_bayes.setText(_translate("MainWindow", "贝叶斯曲线拟合"))
        self.pushButton_probability.setText(_translate("MainWindow", "概率统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "多项式拟合"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "贝叶斯"))
import pics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
