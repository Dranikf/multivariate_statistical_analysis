import numpy as np
import pandas as pd
from common.functions import eig_matlab


def data_stand(x):
    '''стандартизует исходную систему данных по формуле (6.6)'''

    xj = x.mean(axis = 0)
    sigmaj = x.var(axis = 0)**(1/2)

    return (x - xj)/sigmaj


def main_componets(X):
    '''метод главных компонент полностью'''

    # стандартизация исходной системы данных
    z = data_stand(X)

    R = np.corrcoef(X, rowvar = False)
    [L, V] = eig_matlab(R)

    L = L**(1/2)

    A = np.dot(V, L)
    inv_A = np.linalg.inv(A)

    return np.dot(inv_A, z.transpose()).transpose()

def main_componets2(X):
    '''это дублирует предыдущую функцию лишь с тем отличием что
    кроме данных в новой системе координат будет возвращена еще 
    , матрица факторных нагрузок и собсвенные числа корреляционной
    матрицы'''

    # стандартизация исходной системы данных
    z = data_stand(X)

    R = np.corrcoef(X, rowvar = False)
    [L, V] = eig_matlab(R)

    L = L**(1/2)

    A = np.dot(V, L)
    inv_A = np.linalg.inv(A)

    return {'F' : np.dot(inv_A, z.transpose()).transpose(), 'A': A, 'L' : L}