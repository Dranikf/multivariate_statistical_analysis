import numpy as np
import copy


def create_matrix(data, M):
    '''funciton for creating matrix for ssa'''

    if data.shape[0] == 1:
        data = copy.copy(np.transpose(data)) 

    result = np.zeros((M, 1))
    n = len(data)

    for i in range(n - M + 1):
        result = np.hstack((result, np.flip(data[i:M+i])))

    return result[:,1:]

def reconstruct_series(Matrix):
    '''return series average by side diagonals of Matrix '''

    result = []

    M, n = Matrix.shape
    N = n + M - 1
    for t in range(N):
        sum = 0
        if t < M-1:
            for i in range(t+1):
                #print(str(M-t+i-1) + "," + str(i))
                #print(t+1)
                sum += Matrix[M-t+i-1, i]
            result.append(sum/(t+1))
        elif t < N-M+1:
            for i in range(M):
                #print(str(i) + "," + str(t-M+i+1))
                #print(M-1)
                sum += Matrix[i, t-M+i+1]
            result.append(sum/(M-1))
        elif t <= N:
            for i in range(N-t):
                #print(str(i) + "," + str(t-M+i+1))
                #print(N-t)
                sum += Matrix[i, t-M+i+1]
            result.append(sum/(N-t))

    return result



# TESTING OF create_matrix
#test = np.array([[1,2,3,4,5,6,7,8,9,10]])
#print(np.flip(np.transpose(test)))
#print(create_matrix(test, 3))

# TESTING OF reconstruct_series
#matr = np.zeros((4,3))
#matr = np.zeros((3,4))
#reconstruct_series(matr)
#import pandas as pd
#d = pd.read_excel('/home/kfa/KFA/Programming/multivariate_statistical_analysis/ysrs2 ssa/matrixes/new_X_matrix.xlsx').to_numpy()
#print(reconstruct_series(d))