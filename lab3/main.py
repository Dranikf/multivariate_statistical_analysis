import random
import numpy as np
import plotly.graph_objects as go
import copy

import sys
sys.path.append("/home/kfa/KFA/Programming/multivariate_statistical_analysis")
from common.functions import eig_matlab



def rand_creator(matrix):

    result = copy.copy(matrix)

    for i in range(3):
        for j in range(3):
            if i != j:
                result[i,j] = result[i,j] + np.random.uniform(-0.2,0.2,1)[0]

    return result
                

# initial points
matrix = np.array([[1, 0.62, 0.97], [0.62, 1, 0.79], [0.97, 0.79, 1]])
[L, V] = eig_matlab(matrix)


#just a sphere
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
my_sphere = go.Surface(z=z, x=x, y=y, showscale=False, opacity = 0.5)

# markers settings
m1 = go.scatter3d.Marker(size = 5)

# initial points
init_sc1 = go.Scatter3d(x= V[0,:], y = V[1,:], z = V[2,:], mode ='markers', marker = m1, name = "положительные векторы")
init_sc2 = go.Scatter3d(x= -V[0,:], y = -V[1,:], z = -V[2,:], mode ='markers', marker = m1, name = "отрицательные векторы")

# frames creating
points = copy.copy(V)

my_frames = []
for i in range(50):
    [L, V] = eig_matlab(rand_creator(matrix))
    points = np.hstack((points, V))
    #points = np.vstack((points, np.array([0,0,0])))

    my_frames.append(go.Frame(  data = [  my_sphere,
                                        go.Scatter3d(x = points[0,:], y = points[1,:], z = points[2,:], mode ='markers', marker = m1, name = "положительные векторы"),
                                        go.Scatter3d(x = -points[0,:], y = -points[1,:], z = -points[2,:], mode ='markers', marker = m1, name = "отрицательные векторы")]))


#print(points)

# layout settings
layout=go.Layout(
        title = "Изменение +-0,2",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Начать анимацию",method="animate",args=[None])])],
            legend=go.layout.Legend( x=1, y=1, traceorder='normal', font=dict( family='sans-serif', size=20,color='black')))


fig = go.Figure(data=[my_sphere, init_sc1, init_sc2], layout = layout, frames = my_frames)
fig.update_layout(transition = {'duration': 1})


fig.show()