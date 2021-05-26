import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def build_disc(frame1, frame2):
    '''строит дискриминантную функцию - по двум быбркам типа DataFrame'''
    # output:
    #   [c1,c2,...,cn, Y] where Y = x1*c1 + x2*c2 + ...
    s1 = len(frame1)
    s2 = len(frame2)

    f1_np = frame1.to_numpy()
    f2_np = frame2.to_numpy()

    cov1 = np.cov(f1_np, bias = True, rowvar = False)
    cov2 = np.cov(f2_np, bias = True, rowvar = False)

    unioun_cov = (cov1*s1 + cov2*s2) * (1/(s1 + s2 - 2))
    inv_union_cov = np.linalg.inv(unioun_cov)

    mean1 = np.mean(f1_np, axis = 0)
    mean2 = np.mean(f2_np, axis = 0)

    A = np.dot(inv_union_cov,(mean1 - mean2).transpose())

    mean1 = np.dot(f1_np, A).mean()
    mean2 = np.dot(f2_np, A).mean()
    
    #print(np.dot(f1_np, A))
    #print(np.dot(f2_np, A))
    #print(mean1)
    #print(mean2)

    #print((mean1 + mean2)/2)

    A = np.append(A,(mean1 + mean2)/2)

    return A


def get_max_distance(point, array):

    dist = 0

    for i in range(array.shape[0]):
        temp = sqrt(((array[i,:] -  point)**2).sum())
        if dist < temp:
            dist = temp

    return dist


def plot_cirles(frame1, frame2):
    ''' нанесет на трехмерный график точки и построит сферу с центром в усредненной координате и радиусом максимальное расстояние + 1  вернет axis на котором это нанесено'''

    f1_np = frame1.to_numpy()
    f2_np = frame2.to_numpy()

    fig = plt.figure(figsize = [20, 15])
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(f1_np[:,0],f1_np[:,1],f1_np[:,1], s = 100, marker = "o")
    ax.scatter(f2_np[:,0],f2_np[:,1],f2_np[:,1], s = 100, marker = ">")

    cent1 = f1_np.mean(axis = 0)
    cent2 = f2_np.mean(axis = 0)

    d1 = get_max_distance(cent1, f1_np) + 2
    d2 = get_max_distance(cent2, f2_np) + 2

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)

    plot1 = ax.plot_surface(x*d1+cent1[0], y*d1+cent1[1], z*d1+cent1[2])
    plot1.set_alpha(0.3)
    plot2 = ax.plot_surface(x*d2+cent2[0], y*d2+cent2[1], z*d2+cent2[2], color = "orange")
    plot2.set_alpha(0.3)

    return ax
    #plt.show()

def circle_surface(frame1, frame2):
    '''для двух выборок нанесет на график две сферы и поверхность с дискриминантной функцией'''

    f1_np = frame1.to_numpy()
    f2_np = frame2.to_numpy()

    ax = plot_cirles(frame1, frame2)
    A = build_disc(frame1, frame2)
    
    max_x = np.vstack((f1_np[:,0], f2_np[:,0])).max()
    max_y = np.vstack((f1_np[:,1], f2_np[:,1])).max()

    min_x = np.vstack((f1_np[:,0], f2_np[:,0])).min()
    min_y = np.vstack((f1_np[:,1], f2_np[:,1])).min()

    x = np.linspace(min_x, max_x, 30)
    y = np.linspace(min_y, max_y, 30)

    X, Y = np.meshgrid(x, y)

    Z = (A[3] - A[0]*X - A[1]*Y)/(A[2])

    f_pl = ax.plot_surface(X, Y, Z, color = "black")
    f_pl.set_alpha(0.5)

    return ax