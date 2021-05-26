import numpy as np


def create_matrix(data, M):
    '''funciton for creating matrix for ssa'''

    print(np.array([1,2,3]))
    a = np.array([[1,2,3], [1,2,3]])
    n = len(data)

    print(list(range(n-M)))

    for i in range(n - M):
        print(i)
        print(data[i:n+i])