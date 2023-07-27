import matplotlib.pyplot as plt
import numpy as np
from data_reader import *
from mesh_utils import *

def meshplot1(p):
    rows, cols = F.shape
    p = np.array([[F[i, j] for j in range(cols)] for i in range(rows)])
    rowsp, colsp = p.shape
    print('p is ', p)
    print('F is ', F)
    print('size of F is [', rows,',',cols, ']', 'and size of p is [', rowsp, ',', colsp, ']')
    if np.array_equal(p, F) is True:  #其实加不加true都是一样的
        F1 = np.max(F) - np.min(F)
        print('F1 success')

        X, Y = np.meshgrid(x, y)
        plt.set_cmap('jet')

        fig = plt.figure(1)
        plt.show()
        print('fig success')

        # Subplot 1: Surface plot
        ax1 = fig.add_subplot(3, 2, 1, projection='3d')
        ax1.plot_surface(X, Y, F, cmap='jet', shading='interp')
        ax1.set_zlabel('Flatness(μm)')
        ax1.set_xlabel('表面平面度=' + str(F1) + ' μm')

        # Subplot 2: Contour plot
        ax2 = fig.add_subplot(3, 2, 2)
        contour = ax2.contourf(X, Y, F, 30)
        plt.colorbar(contour)
        plt.show()
        print('print success')
    else:
        print('no match')

refactor1(F)
meshplot1(F)
plt.show()
