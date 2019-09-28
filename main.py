from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from prmlTest import MainWindow

from scipy import _distributor_init
# from scipy import spatial.ck

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
    input("输入任意键结束")