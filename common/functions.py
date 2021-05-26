import numpy as np

def eig_matlab(M):
    '''по полученной матрице M возвращает собственные занчения и собственные числа в формате как MatLab'''
    lmdas, vectors = np.linalg.eig(M)
    L = np.zeros(len(lmdas))


    for i,l in enumerate(lmdas):
        temp = np.zeros(len(lmdas))
        temp[i] = l
        L = np.vstack((L, temp))

    #print(L)
    L = L[1:]

    return [L, vectors]