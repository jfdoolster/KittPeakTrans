"""
main plotter
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from kittpeak import proccess_kittpeak_data

COLOR = 'black'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR
mpl.rcParams['figure.figsize'] = (24,6)
mpl.rcParams['lines.linewidth'] = 1.0
#mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['purple', 'g', 'r', 'c', 'm', 'y', 'k'])

if __name__ == "__main__":

    if not os.path.exists('plots/'):
        os.makedirs('plots/')

    df_full,_,_ = proccess_kittpeak_data()
    print(df_full)
    df_full.info()

    print('creating plots/wavelength_0_5-1_5.png ...')
    fig = plt.figure()
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(0.5, 1.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_0_5-1_5.png', transparent=True)

    print('creating plots/wavelength_1_5-2_5.png ...')
    fig = plt.figure()
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(1.5, 2.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_1_5-2_5.png', transparent=True)

    print('creating plots/wavelength_2_5-3_5.png ...')
    fig = plt.figure()
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(2.5, 3.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_2_5-3_5.png', transparent=True)

    print('creating plots/wavelength_3_5-4_5.png ...')
    fig = plt.figure()
    plt.plot(df_full['Wavelength [um]'], df_full['Transmission'], linewidth=0.1)
    plt.xlim(3.5, 4.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plots/wavelength_3_5-4_5.png', transparent=True)

    plt.show()
