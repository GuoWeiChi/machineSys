# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette,QColor

from Ui_prml import Ui_MainWindow

import numpy as np
import matplotlib.pyplot as plt

import time

from MulNoiseData import MulNoiseDataDlg

from prml.preprocess import PolynomialFeature
from prml.linear import (
    LinearRegression,
    RidgeRegression,
    BayesianRegression
)

import linaRegression


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.myDlg = MulNoiseDataDlg()
        self.myDlg1 = linaRegression.Dialog()
        self.setupUi(self)
        #self.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        #self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        self.setAutoFillBackground(True)

        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色

        self.setPalette(pe)
        self.pushButtonMul.setStyleSheet('''QPushButton{background:#3399cc;border-radius:15px;}
        QPushButton:hover{background:#3366cc;}''')
        self.pushButtonMul.setIconSize(QSize(30, 30))

        self.pushButtonLine.setStyleSheet('''QPushButton{background:#3399cc;border-radius:15px;}
               QPushButton:hover{background:#3366cc;}''')
        self.pushButtonLine.setIconSize(QSize(30, 30))

        self.pushButtonLine_bayes.setStyleSheet('''QPushButton{background:#3399cc;border-radius:15px;}
                       QPushButton:hover{background:#3366cc;}''')
        self.pushButtonLine_bayes.setIconSize(QSize(30, 30))

        self.pushButton_probability.setStyleSheet('''QPushButton{background:#3399cc;border-radius:15px;}
                                      QPushButton:hover{background:#3366cc;}''')
        self.pushButton_probability.setIconSize(QSize(30, 30))

        self.tabWidget.setStyleSheet('''background:#C0C0C0''')



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
    def on_pushButtonMul_clicked(self):
        self.myDlg.show()
        """
        Slot documentation goes here.
        """

    @pyqtSlot()
    def on_pushButtonLine_clicked(self):
        self.myDlg1.show()

    @pyqtSlot()
    def on_pushButtonLine_bayes_clicked(self):
        np.random.seed(1234)
        # 产生训练数据和测试数据,标准差是0.25
        x_train, y_train = self.create_toy_data(self.func, 10, 0.25)
        # 测试数据:从0到1一共100个数据
        x_test = np.linspace(0, 1, 100)
        # 计算标准的测试数据的值
        y_test = self.func(x_test)

        feature = PolynomialFeature(9)
        X_train = feature.transform(x_train)
        X_test = feature.transform(x_test)

        model = BayesianRegression(alpha=2e-3, beta=2)
        model.fit(X_train, y_train)

        y, y_err = model.predict(X_test, return_std=True)
        plt.scatter(x_train, y_train, facecolor="none", edgecolor="b", s=50, label="training data")
        plt.plot(x_test, y_test, c="g", label="$\sin(2\pi x)$")
        plt.plot(x_test, y, c="r", label="mean")
        plt.fill_between(x_test, y - y_err, y + y_err, color="pink", label="std.", alpha=0.5)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-1.5, 1.5)
        plt.annotate("M=9", xy=(0.8, 0.5))
        plt.legend(bbox_to_anchor=(0.7, 1.), loc=2, borderaxespad=0.)
        plt.show()