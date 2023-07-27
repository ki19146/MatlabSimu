# THIS IS FOR DEFINE FUNCTIONS TO GENERATE THE 3D MESH CURVE

import numpy as np
import matplotlib.pyplot as plt
from data_reader import *


# ANNOTATION BLOCK: SEE IN main.py


# refactor1() BLOCK:
def refactor1(p):
    h, l = p.shape                    # ASSIGN NUMPY ARRAY DIMENSIONS TO h,l
    p = p[4:h, :]
    h, l = p.shape
    a = np.isnan(p)                   # CHECK NaN VALUES IN NUMPY ARRAY
    u, v = np.where(a == False)       # GET INDICES OF non-NaN
    h1, l1 = u[0], v[0]
    p = p[h1:h, l1:l]                 # NUMPY ARRAY SLICING TO OBTAIN SUBMATRIX
    hs, ls = p.shape
    #x = np.linspace(0, hs - 1, hs)   # COMMENT FOR NOT USE
    cd = (ls - 1) * 1
    kd = (hs - 1) * 1
    global x,y
    x = np.linspace(0, cd, ls)
    y = np.linspace(0, kd, hs)
    print('refactor1 success')
    print('x and y is', x,y)
    return x, y                       # COMMENT THIS LINE IF NOT USING x,y OUTSIDE THE def FUNCTION


# MESH PLOT BLOCK:
def meshplot(p):
    global fig
    if np.array_equal(p, F):
        F1 = np.max(p) - np.min(p)

        X, Y = np.meshgrid(x, y)
        plt.set_cmap('jet')

        fig = plt.figure(1,figsize=(12,8))

        # Subplot 1: Surface plot
        ax1 = fig.add_subplot(3, 2, 1, projection='3d')
        ax1.plot_surface(X, Y, F, cmap='jet', shading='interp')
        ax1.set_zlabel('Flatness(μm)')
        ax1.set_xlabel('表面平面度=' + str(F1) + ' μm')

        # Subplot 2: Contour plot
        ax2 = fig.add_subplot(3, 2, 2)
        contour = ax2.contourf(X, Y, F, 30)
        plt.colorbar(contour)
        plt.ion()
        plt.show()

    elif np.array_equal(p, B):
        B1 = np.max(p) - np.min(p)

        X, Y = np.meshgrid(x, y)
        plt.set_cmap('jet')

        fig = plt.figure(1)

        # Subplot 1: Surface plot
        ax1 = fig.add_subplot(3, 2, 3, projection='3d')
        ax1.plot_surface(X, Y, B, cmap='jet', shading='interp')
        ax1.set_zlabel('Flatness(μm)')
        ax1.set_xlabel('里面平面度=' + str(B1) + ' μm')

        # Subplot 2: Contour plot
        ax2 = fig.add_subplot(3, 2, 4)
        contour = ax2.contourf(X, Y, B, 30)
        plt.colorbar(contour)
        plt.show()

    elif np.array_equal(p, T):
        TTV = np.max(T) - np.min(T)
        MaxThk = np.max(T)
        MinThk = np.min(T)
        AveThk = np.mean(T)

        X, Y = np.meshgrid(x, y)
        plt.set_cmap('jet')

        fig = plt.figure(1)

        # Subplot 1: Surface plot
        ax1 = fig.add_subplot(3, 2, 5, projection='3d')
        ax = plt.gca()  # GET CURRENT AXIS
        z_ticks = ax.get_zticks()
        z_tick_labels = [f'{tick:d}' for tick in z_ticks]
        ax.set_zticklabels(z_tick_labels)
        ax1.plot_surface(X, Y, T, cmap='jet', shading='interp')
        labels = [
            f'MaxThk = {MaxThk} μm'
            f'MinThk = {MinThk} μm'
            f'AveThk = {AveThk} μm'
        ]
        ax1.set_ylabel(labels)
        ax1.set_xlabel('TTV=' + str(TTV) + ' μm')

        # Subplot 2: Contour plot
        ax2 = fig.add_subplot(3, 2, 6)
        contour = ax2.contourf(X, Y, T, 30)
        plt.colorbar(contour)
        plt.show()

    # return fig
    #return X, Y



