import matplotlib as plt
import numpy as np


def just_plot_sphere(center, r , ax, **kwargs):
    '''center - центр сферы
        r - радиус сферы
        ax - оси на которых следует нарисовать сферу'''

    u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)

    plot1 = ax.plot_wireframe(x*r+center[0], y*r+center[1], z*r+center[2], **kwargs)

    return plot1