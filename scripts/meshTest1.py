import numpy as np
import matplotlib.pyplot as plt
from data_reader import *

def meshplot(p):
    global fig
    if np.array_equal(p, F):
        F1 = np.max(p) - np.min(p)

        X, Y = np.meshgrid(x, y)
        plt.set_cmap('jet')

        fig = plt.figure(1, figsize=(12, 8))

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
    # return X, Y