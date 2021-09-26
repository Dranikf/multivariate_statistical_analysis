import numpy as np;

def to_simetric(matrix, rule):
    '''function from numpy matrix creates simetric matrix by using setted rule'''
    # inputs:
    # <matrix> - matrix for transformation
    # <rule> -  function wich takes 2 arguments matrix[i,j] and matrix[j,i] and retrun single value
    #           wich takes resutl[i,j] and result[j,i]. Look half_rule funciton for example. 
    # optput - transformated resutl matrix

    result_list = []

    for i in range(matrix.shape[0]):
        result_list.append([]);
        for j in range(matrix.shape[1]):
            if i != j:
                result_list[i].append(rule(matrix[i,j],matrix[j,i]));
            else:
                result_list[i].append(0);

    return np.matrix(result_list);

def half_rule(ij, ji):
    return (ij + ji) /2;


#EXAMPLE
#a = np.matrix([[1,2,3,4], [6,5,2,3],[3,4,5,2], [2,3,4,5]])
#res = to_simetric(a, half_rule)

#print(a);
#print(res);