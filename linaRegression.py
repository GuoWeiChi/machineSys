# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot,QRegExp
from PyQt5.Qt import QRegExpValidator
from PyQt5.QtWidgets import QDialog,QMessageBox

from Ui_linaRegression import Ui_Dialog

import numpy as np
import matplotlib.pyplot as plt


from prml.preprocess import PolynomialFeature
from prml.linear import (
    LinearRegression,
    RidgeRegression,
    BayesianRegression
)

import time

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
        self.normalFlag = False
        self.setupUi(self)
        self.lineEditLambda.setVisible(False)
        self.lambdaInfo.setVisible(False)
        self.regExp = QRegExp("^(-?\d+)(\.\d+)?$")  # 创建了一个模式
        self.validator = QRegExpValidator(self.regExp)
        self.lineEditLambda.setValidator(self.validator)
        self.lineEditNum.setValidator(self.validator)
        self.lineEditPower.setValidator(self.validator)


    # 创建随机数据
    def create_toy_data(self,func, sample_size, std):
        # 生成数据在0-1之间,sample_size个数据,包括1
        x = np.linspace(0, 1, sample_size)
        # 生成数据加上随机高斯噪声
        t = func(x) + np.random.normal(scale=std, size=x.shape)
        # 把x和t的值返回
        return x, t

    # sin(2*π*x)
    def func(self,x):
        return np.sin(2 * np.pi * x)

    @pyqtSlot()
    def on_pushButtonStart_clicked(self):
        if self.isNormal.isChecked():
            try:
                num = int(self.lineEditNum.text())
                if num < 1:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return
                if num > 100:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return

                power = int(self.lineEditPower.text())
                if power < 0:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return
                if power > 15:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return

                np.random.seed(int(time.time()))
                # 产生训练数据和测试数据,标准差是0.25
                x_train, y_train = self.create_toy_data(self.func, num, 0.25)
                # 测试数据:从0到1一共100个数据
                x_test = np.linspace(0, 1, 100)
                # 计算标准的测试数据的值
                y_test = self.func(x_test)

                # 转换具有多项式特征的输入数组
                #  [1,x,x^2...,x^i]
                feature = PolynomialFeature(power)
                # 分别求对应的多少次方
                # [x_train^0,x_train^1,x_train^2,...]
                X_train = feature.transform(x_train)
                # 测试数据转换成具有多项式特征的输入数组
                X_test = feature.transform(x_test)
                # 正则化 lambda = 1e-3
                lam = float(self.lineEditLambda.text())
                model = RidgeRegression(alpha=lam)
                model.fit(X_train, y_train)
                y = model.predict(X_test)

                plt.scatter(x_train, y_train, facecolor="none", edgecolor="b", s=50, label="training data")
                plt.plot(x_test, y_test, c="g", label="$\sin(2\pi x)$")
                plt.plot(x_test, y, c="r", label="fitting")
                plt.ylim(-1.5, 1.5)
                plt.legend()
                plt.annotate("M=9", xy=(-0.15, 1))
                plt.show()
                pass
            except:
                QMessageBox.warning(self, "提示", "请输入一个整数")
        else:
            try:
                num = int(self.lineEditNum.text())
                if num < 1:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return
                if num > 100:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return

                power = int(self.lineEditPower.text())
                if power < 0:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return
                if power > 15:
                    QMessageBox.warning(self, "提示", "输入有误,请重新输入")
                    return

                np.random.seed(int(time.time()))

                # 产生训练数据和测试数据,标准差是0.25
                x_train, y_train = self.create_toy_data(self.func, num , 0.25)
                # 测试数据:从0到1一共100个数据
                x_test = np.linspace(0, 1, 100)
                # 计算标准的测试数据的值
                y_test = self.func(x_test)

                # 不同次数的拟合
                # 转换具有多项式特征的输入数组
                # [1,x,x^2...]
                feature = PolynomialFeature(power)
                # 分别求对应的多少次方
                # [x_train^0,x_train^1,x_train^2,...]
                X_train = feature.transform(x_train)
                # 转换具有多项式特征的输入数组
                X_test = feature.transform(x_test)
                # 线性回归模型
                model = LinearRegression()
                # 最小二乘拟合
                model.fit(X_train, y_train)
                # 预测X_test
                y = model.predict(X_test)
                # 绘制训练的点,蓝色
                plt.scatter(x_train, y_train, facecolor="none", edgecolor="b", s=50, label="training data")
                # 绘制测试的真实数据,绿色
                plt.plot(x_test, y_test, c="g", label="$\sin(2\pi x)$")
                # 绘制预测的数据,红色
                plt.plot(x_test, y, c="r", label="fitting")
                # y轴范围
                plt.ylim(-1.5, 1.5)
                # 添加标注
                plt.annotate("M={}".format(power), xy=(0.5, 1))

                # 添加注释
                plt.legend(bbox_to_anchor=(0.65, 1.0), loc=2, borderaxespad=0.)
                plt.show()
            except:
                QMessageBox.warning(self, "提示", "请输入一个整数")

    @pyqtSlot()
    def on_isNormal_clicked(self):
        if self.isNormal.isChecked():
            self.lineEditLambda.setVisible(True)
            self.lambdaInfo.setVisible(True)
            self.lineEditLambda.setText("0.003")


        else:
            self.lineEditLambda.setVisible(False)
            self.lambdaInfo.setVisible(False)

            # 均方误差

    def rmse(self,a, b):
        return np.sqrt(np.mean(np.square(a - b)))

    @pyqtSlot()
    def on_pushButtonErrStatistic_clicked(self):
        #产生训练数据和测试数据,标准差是0.25
        x_train, y_train = self.create_toy_data(self.func, 10, 0.25)
        #测试数据:从0到1一共100个数据
        x_test = np.linspace(0, 1, 100)
        #计算标准的测试数据的值
        y_test = self.func(x_test)



        #训练集error
        training_errors = []
        #测试集error
        test_errors = []


        for i in range(10):
            # 转换具有多项式特征的输入数组
            # [1,x,x^2...,x^i]
            feature = PolynomialFeature(i)
            # 分别求对应的多少次方
            # [x_train^0,x_train^1,x_train^2,...]
            X_train = feature.transform(x_train)
            # 测试数据转换成具有多项式特征的输入数组
            X_test = feature.transform(x_test)

            #线性回归
            model = LinearRegression()
            #训练模型
            model.fit(X_train, y_train)
            #预测模型
            y = model.predict(X_test)
            #记录训练数据的最小误差
            training_errors.append(self.rmse(model.predict(X_train), y_train))
            #记录测试数据的误差
            test_errors.append(self.rmse(model.predict(X_test), y_test + np.random.normal(scale=0.25, size=len(y_test))))

        #训练数据
        plt.plot(training_errors, 'o-', mfc="none", mec="b", ms=10, c="b", label="Training")
        #测试数据
        plt.plot(test_errors, 'o-', mfc="none", mec="r", ms=10, c="r", label="Test")
        plt.legend()
        plt.xlabel("degree")
        plt.ylabel("RMSE")
        plt.show()

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = Dialog()
    myWin.show()
    sys.exit(app.exec_())
    

