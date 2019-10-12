# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_DiagLogisticReression import Ui_Dialog

from sklearn import linear_model

from PyQt5.QtWidgets import QMessageBox

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)


    @pyqtSlot()
    def on_pushButton_predict_clicked(self):
        X = []
        Y = []
        for i in range(self.tableWidget.rowCount()-1):
                # print(self.tableWidget.item(i, j).text())
                X.append([int(self.tableWidget.item(i, 0).text()),int(self.tableWidget.item(i, 1).text())])
                Y.append(int(self.tableWidget.item(i, 2).text()))

        lr = linear_model.LogisticRegression()
        lr.fit(X, Y)
        testX = [[int(self.lineEdit_age.text()), int(self.lineEdit_income.text())]]
        label = lr.predict(testX)
        theta_0 = lr.intercept_
        theta_1 = lr.coef_[0][0]
        theta_2 = lr.coef_[0][1]


        msg = "theta_0:" + str(theta_0) +"   theta_1:"+str(theta_1) + "   theta_2:"+str(theta_2)
        QMessageBox.information(self, "theta", msg, QMessageBox.Yes | QMessageBox.No)
        # QMessageBox.information(self, "消息框标题", "这是一条消息。", QMessageBox.Yes | QMessageBox.No)
        self.res.setText("预测的结果为:"+str(label[0]))
        #
        # lr = linear_model.LogisticRegression()
        # lr.fit(X,Y)
        # testX = [[28,8]]
        # print("predicted label = ",label)
        # prob = lr.predict_proba(testX)
        # print("probability = ",prob)

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
# from mainWindow import MainWindow

from scipy import _distributor_init
# from scipy import spatial.ck



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = Dialog()
    myWin.show()
    sys.exit(app.exec_())
    input("输入任意键结束")
    

