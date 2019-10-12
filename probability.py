# -*- coding: utf-8 -*-

"""
Module implementing probabilityDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_probability import Ui_Dialog

from includes import *

class probabilityDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(probabilityDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButtonBia_clicked(self):
        model = Bernoulli()
        model.fit(np.array([0., 1., 1., 1.]))
        print(model)
        pass

    @pyqtSlot()
    def on_pushButtonBeta_clicked(self):
        x = np.linspace(0, 1, 100)
        for i, [a, b] in enumerate([[0.1, 0.1], [1, 1], [2, 3], [8, 4]]):
            plt.subplot(2, 2, i + 1)
            beta = Beta(a, b)
            plt.xlim(0, 1)
            plt.ylim(0, 3)
            plt.plot(x, beta.pdf(x))
            plt.annotate("a={}".format(a), (0.1, 2.5))
            plt.annotate("b={}".format(b), (0.1, 2.1))
        plt.show()

    @pyqtSlot()
    def on_pushButtonLogCurve_clicked(self):
        x = [float(i)/100.0 for i in range(1,300)]
        y=[math.log(i) for i in x]
        plt.plot(x,y,'r-',linewidth=3,label='log Curve')
        a=[x[20],x[175]]
        b = [y[20],y[175]]
        plt.plot(a,b,'g-',linewidth=2)
        plt.plot(a,b,'b+',markersize=15,alpha=0.75)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('log(x)')
        plt.show()

    @pyqtSlot()
    def on_pushButtonAvg_clicked(self):
        u = np.random.uniform(0.0, 1.0, 10000)
        plt.hist(u, 80, facecolor='g', alpha=0.75)
        plt.grid(True)
        plt.show()

    @pyqtSlot()
    def on_pushButtonGauss_clicked(self):
        u = np.random.uniform(0.0, 1.0, 10000)
        times = 10000
        for time in range(times):
            u += np.random.uniform(0.0,1.0,10000)
        u /= times
        plt.hist(u,80,facecolor='g',alpha=0.75)
        plt.grid(True)
        plt.show()

    def calcEM(self,height):
        # N = len(height)
        # gp = 0.5
        # bp = 0.5
        # gmu,gsigma = min(height),1 #先验,直接取最大和最小值
        # bmu,bsigma = max(height),1
        # ggamma = range(N)
        # bgamma = range(N)
        # cur = [gp,bp,gmu,gsigma,bmu,bsigma]
        #
        # times = 0
        # while times < 100:
        #     i=0
        #     for x in height:
        #         ggamma[i] = gp*gauss(x,gnu,gsigma)
        pass

    @pyqtSlot()
    def on_pushButtonEM_clicked(self):
        pass

    def calc(self,data):
        n = len(data)
        #期望
        niu = 0.0
        #二次方的均值,用于求方差
        niu2 = 0.0
        #三次方的均值
        niu3 = 0.0
        for a in data:
            niu += a
            niu2 += a**2
            niu3 += a**3
        niu /= n
        niu2 /= n
        niu3 /= n
        sigma = math.sqrt(niu2 - niu*niu)
        return [niu,sigma,niu3]


    def calc_stat(self,data):
        [niu,sigma,niu3] = self.calc(data)
        n = len(data)
        #4阶中心矩
        niu4 = 0.0
        for a in data:
            a -= niu
            niu4 += a**4
        niu4 /= n



        #偏度
        skew = (niu3 - 3*niu*sigma**2 - niu**3) / (sigma ** 3)
        #峰度
        kurt = niu4 / (sigma ** 4)

        s = pd.Series(data)
        print("skew=", s.skew(), "       kurt=", s.kurt())
        return [niu,sigma,skew,kurt]

    @pyqtSlot()
    def on_pushButtonVar_clicked(self):
        data = list(np.random.randn(10000))
        data2 = [x*10 for x in data]
        data3 = [x for x in data if x > -0.5]
        data4 = list(np.random.uniform(0,4,10000))

        [niu,sigma,skew,kurt] = self.calc_stat(data)
        [niu2, sigma2, skew2, kurt2] = self.calc_stat(data2)
        [niu3, sigma3, skew3, kurt3] = self.calc_stat(data3)
        [niu4, sigma4, skew4, kurt4] = self.calc_stat(data4)

        plt.subplot(2,2,1)
        info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.5f,\ kurt=%.5f$' % (niu, sigma, skew, kurt)
        plt.title(info)
        plt.hist(data, 50, normed=True, facecolor='gray', alpha=0.9)
        plt.grid(True)

        plt.subplot(2, 2, 2)
        info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.5f,\ kurt=%.5f$' % (niu2, sigma2, skew2, kurt2)
        plt.title(info)
        plt.hist(data, 50, normed=True, facecolor='pink', alpha=0.3)
        plt.hist(data2, 50, normed=True, facecolor='gray', alpha=0.9)
        plt.grid(True)

        plt.subplot(2, 2, 3)
        info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu3, sigma3, skew3, kurt3)
        plt.title(info)
        plt.hist(data, 50, normed=True, facecolor='pink', alpha=0.7)
        plt.hist(data3, 50, normed=True, facecolor='gray', alpha=0.9)
        plt.grid(True)

        plt.subplot(2, 2, 4)
        info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu4, sigma4, skew4, kurt4)
        plt.title(info)
        plt.hist(data, 50, normed=True, facecolor='pink', alpha=0.7)
        plt.hist(data4, 50, normed=True, facecolor='gray', alpha=0.9)
        plt.grid(True)

        plt.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = probabilityDialog()
    myWin.show()
    sys.exit(app.exec_())
    input("输入任意键结束")
    

