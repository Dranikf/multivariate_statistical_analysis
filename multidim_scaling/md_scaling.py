import numpy as np;
import sys;
sys.path[0] = '/home/dranik/KFA/programming/multivariate_statistical_analysis';

import lab2.main_comp as mc;
from copy import copy;

def normalize_data(data):
    '''funciton for normalisation given data'''
    #inputs:
    #<data> - data as np array
    # outputs:
    #<norm_data> - normalised data

    result = copy(data)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            result[i,j] = data[i,j]/np.mean(data[:,j]);
    
    return result;

def eucl_distance(p1, p2):
    return(np.sum(np.square(p1-p2))**(1/2))

def object_distances(data, dist_fun = eucl_distance):
    '''fucniton for computing pair distances'''
    #inputs:
    #<data> - data about objects where objects in lines
    #<dist_fun> -   funciton for computing distances wich takes two numpy.array with lines
    #               the Euclidean distance is selected by default
    #outputs - numpy.array wich contains pair distances

    n = data.shape[0];

    result = np.zeros(shape = (n,n))

    for i in range(n):
        for j in range(i, n):
            result[i,j] = dist_fun(data[i,:], data[j,:])
            result[j,i] = result[i,j]

    return result



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
    '''simpliest rule for <to_simetric> funciton. Just returns mean for opposing elements '''
    return (ij + ji) /2;

#EXAMPLE
#a = np.matrix([[1,2,3,4], [6,5,2,3],[3,4,5,2], [2,3,4,5]])
#res = to_simetric(a, half_rule)

#print(a);
#print(res);


def b_matrix(comp_matr):
    '''function realises matrix transformation from matrix pairs comparison to b matrix'''
    # inputs:
    # <comp_matr> - simetric matrix with comparison comp_matr[i, j] = comp_matr[j, i] characterize the similarity of object(i) and object(j)
    # outputs - transformed matrix needed for required coordinates

    result = copy(comp_matr);

    n = comp_matr.shape[0];
    # sum of squares matrix elements
    mat_ss = np.square(comp_matr).sum();


    for i in range(n):
        for j in range(i, n):
            line_sq_sum = np.square(comp_matr[i,:]).sum();
            col_sq_sum = np.square(comp_matr[:,j]).sum();
            result[i,j] = -(1/2)*(comp_matr[i,j]**2 - ((1/n)*line_sq_sum + (1/n)*col_sq_sum) + (1/(n**2))*mat_ss);
            result[j,i] = result[i,j];

    return result;
            



mat = np.matrix([[0, 2.47, 2.38],[2.47, 0, 1.54],[2.38, 1.54, 0]]);
B = b_matrix(mat);
res = mc.main_componets2(B);
print(res['A'])