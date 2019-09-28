from PyQt5.QtCore import pyqtSlot,QRegExp
from PyQt5.Qt import QRegExpValidator
from PyQt5.QtWidgets import QDialog,QMessageBox

import numpy as np
import matplotlib.pyplot as plt


from prml.preprocess import PolynomialFeature
from prml.linear import (
    LinearRegression,
    RidgeRegression,
    BayesianRegression
)


import numpy as np
import matplotlib.pyplot as plt

from prml.rv import (
    Bernoulli,
    Beta,
    Categorical,
    Dirichlet,
    Gamma,
    Gaussian,
    MultivariateGaussian,
    MultivariateGaussianMixture,
    StudentsT,
    Uniform
)

import time


from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from prmlTest import MainWindow

from scipy import _distributor_init

import math
# from scipy import spatial.ck