import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import ascii
from scipy.constants import *

#df1 = ascii.read('transdata_1_5_mic',
#		names=['Wavenumber','Transmission'])
#df2 = ascii.read('transdata_0.5_1_mic',
#		names=['Wavenumber','Transmission'])
#
#ascii.write(df1,'TransData_1_5.csv',overwrite=True)
#ascii.write(df2,'TransData_05_1.csv',overwrite=True)

LongWave  = pd.read_csv('TransData_1_5.csv',sep=' ')
ShortWave = pd.read_csv('TransData_05_1.csv',sep=' ')

FULL = LongWave.merge(ShortWave,)






upp = 1/1.1E-6
low = 1/2.4E-6


plt.show()

