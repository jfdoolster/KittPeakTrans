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
mpl.rcParams['figure.figsize'] = (24,6)

if __name__ == "__main__":

    if not os.path.exists('plots/'):
        os.makedirs('plots/')

    df_full,_,_ = proccess_kittpeak_data()
    print(df_full)
    print(df_full.info())

    fig = plt.figure()
    fig.set_size_inches(24,6)
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(0.5, 1.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_0_5-1_5.png', transparent=True)

    fig = plt.figure()
    fig.set_size_inches(24,6)
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(1.5, 2.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_1_5-2_5.png', transparent=True)

    fig = plt.figure()
    fig.set_size_inches(24,6)
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(2.5, 3.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_2_5-3_5.png', transparent=True)

    fig = plt.figure()
    fig.set_size_inches(24,6)
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(3.5, 4.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_3_5-4_5.png', transparent=True)