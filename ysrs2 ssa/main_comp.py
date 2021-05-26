import numpy as np
import pandas as pd


def data_stand(x):
    '''стандартизует исходную систему данных по формуле (6.6)'''

    xj = x.mean(axis = 0)
    sigmaj = x.var(axis = 0)**(1/2)

    return (x - xj)/sigmaj


def eig_matlab(M):
    '''по полученной матрице M возвращает собственные занчения и собственные числа в формате как MatLab'''
    lmdas, vectors = np.linalg.eigh(M)
    d1, d2 = M.shape
    L = np.zeros((d1))


    for i,l in enumerate(lmdas):
        temp = np.zeros(len(lmdas))
        temp[i] = l
        L = np.vstack((L, temp))

    L = L[1:]

    return [L, vectors]


def main_componets(X):
    '''метод главных компонент польностью'''

    # стандартизация исходной системы данных
    z = data_stand(X)

    R = np.corrcoef(X, rowvar = False)
    [L, V] = eig_matlab(R)

    L = L**(1/2)

    A = np.dot(V, L)
    inv_A = np.linalg.inv(A)

    return np.dot(inv_A, z.transpose()).transpose()