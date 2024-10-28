"""
main plotter
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from kittpeak import proccess_kittpeak_data

COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR
mpl.rcParams['figure.figsize'] = (33.1,23.4)
mpl.rcParams['lines.linewidth'] = 0.1
plt.rcParams['axes.facecolor'] = 'black'
#mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['purple', 'g', 'r', 'c', 'm', 'y', 'k'])

if __name__ == "__main__":

    if not os.path.exists('plots/'):
        os.makedirs('plots/')

    df_full,_,_ = proccess_kittpeak_data()
    print(df_full)
    df_full.info()

    print('creating plots/wavelength_0_5-1_5.png ...')
    fig = plt.figure()
    axs = fig.subplots(4,1)

    axs[0].plot(df_full['Wavelength [um]'], df_full['Transmission'], zorder=1)
    axs[0].set_xlim(0.5, 1.5)

    axs[1].plot(df_full['Wavelength [um]'], df_full['Transmission'], zorder=1)
    axs[1].set_xlim(1.5, 2.5)

    axs[2].plot(df_full['Wavelength [um]'], df_full['Transmission'], zorder=1)
    axs[2].set_xlim(2.5, 3.5)

    axs[3].plot(df_full['Wavelength [um]'], df_full['Transmission'], zorder=1)
    axs[3].set_xlim(3.5, 4.5)

    for ax in axs:
        ax.grid(True, zorder=0.1, alpha=0.7)
    fig.tight_layout()

    plt.show()
