import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
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
    df_full.info()

    print('creating plots/wavelength_sif.png ...')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(df_full['Wavelength [um]']*1.E3, df_full['Transmission'], linewidth=0.2)
    ax1.set_xlim(450, 750)
    ax1.grid(True)

    x = np.arange(380, 750, 1)

    MAP = 'nipy_spectral'
    NPOINTS = len(x)

    #ax1.set_prop_cycle(plt.get_cmap(MAP))
    ax1.axvspan(min(x), max(x), alpha=0.1, color='gray')

    fig.tight_layout()
    fig.savefig('plots/wavelength_sif.png', transparent=False)
    plt.show()