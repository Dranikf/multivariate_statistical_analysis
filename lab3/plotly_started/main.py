import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from random import random

df = px.data.iris()

#just a sphere
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

#fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, showscale=False, opacity = 0.4), px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')])
my_sc = go.Scatter3d(x= [1], y = [2], z =[1])
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, showscale=False, opacity = 0.4), my_sc])


fig.show()