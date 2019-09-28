# -*- coding: utf-8 -*-

"""
Module implementing MulNoiseDataDlg.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QMessageBox

from Ui_MulNoiseData import Ui_Dialog


import numpy as np
import matplotlib.pyplot as plt

import time

from prml.preprocess import PolynomialFeature
from prml.linear import (
    LinearRegression,
    RidgeRegression,
    BayesianRegression
)


class MulNoiseDataDlg(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MulNoiseDataDlg, self).__init__(parent)
        self.setupUi(self)

# 创建随机数据
    def create_toy_data(self, func, sample_size, std):
        # 生成数据在0-1之间,sample_size个数据,包括1
        x = np.linspace(0, 1, sample_size)
        # 生成数据加上随机高斯噪声
        t = func(x) + np.random.normal(scale=std, size=x.shape)
        # 把x和t的值返回
        return x, t

    # sin(2*π*x)
    def func(self, x):
        return np.sin(2 * np.pi * x)

    @pyqtSlot()
    def on_pushButtonStart_clicked(self):
        """
        Slot documentation goes here.
        """

        try:
            num = int(self.lineEditNum.text())
            if num <= 0:
                QMessageBox.warning(self, "提示", "请输入一个大于0的整数,范围在[1-50]")
                return
            if num > 50:
                QMessageBox.warning(self, "提示", "请输入一个小于等于50的整数,范围在[1-50]")
                return

            np.random.seed(int(time.time()))
            # 产生训练数据和测试数据,标准差是0.25
            x_train, y_train = self.create_toy_data(self.func, num, 0.25)
            # 测试数据:从0到1一共100个数据
            x_test = np.linspace(0, 1, 100)
            # 计算标准的测试数据的值
            y_test = self.func(x_test)

            # 绘制测试数据的点
            plt.scatter(x_train, y_train, facecolor="none", edgecolor="b", s=50, label="training data")
            # 绘制测试数据的线条
            plt.plot(x_test, y_test, c="g", label="$\sin(2\pi x)$")
            # 右上角显示名称
            plt.legend()
            plt.show()
        except:
            QMessageBox.warning(self, "提示", "请输入一个整数")



from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = MulNoiseDataDlg()
    myWin.show()
    sys.exit(app.exec_())