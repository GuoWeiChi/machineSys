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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = probabilityDialog()
    myWin.show()
    sys.exit(app.exec_())
    input("输入任意键结束")
    

