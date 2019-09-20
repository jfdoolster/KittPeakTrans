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

#LongWave  = pd.read_csv('TransData_1_5.csv',sep=' ')
#ShortWave = pd.read_csv('TransData_05_1.csv',sep=' ')
#
#FULL = pd.concat([LongWave,ShortWave],ignore_index=True)
#FULL['Wavelength'] = [10**4/x for x in FULL['Wavenumber']]
#FULL['Frequency'] = [c/(x*10**-6) for x in FULL['Wavelength']]
#
#FULL.loc[FULL['Transmission'] < 0, 'Transmission'] = 0.0
#FULL.loc[FULL['Transmission'] > 1, 'Transmission'] = 1.0
#FULL.to_csv('KittPeak.csv',index=False)

FULL = pd.read_csv('KittPeak.csv',sep=',')


def PlotEm(name='Wavelength',RANGE=[0.5,2.5]):

	if name in list(FULL):
		if name == 'Wavelength':
			print('micrometers')
		if name == 'Wavenumber':
			print('cm^-1')
			RANGE = [10**4/x for x in (RANGE[1],RANGE[0]) ]
		if name == 'Frequency':
			print('Hz')
			RANGE = [c/(x*10**-6) for x in (RANGE[1],RANGE[0]) ]

		NEW = FULL.loc[(FULL[name] >= RANGE[0]) & (FULL[name] <= RANGE[1])]

		plt.grid(True)
		plt.plot(NEW[name],NEW['Transmission'],linewidth=0.1)
		plt.ylabel(r'Transmission')
		plt.xlabel(r'Wavelength [$\mu$m]')
		plt.xlim((RANGE[0],RANGE[1]))
		plt.show()

	else:
		print('Check Spelling er something.')

PlotEm('Wavelength')
#PlotEm('Wavenumber')
#PlotEm('Frequency')


