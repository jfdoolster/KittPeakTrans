"""
docstring
"""

import copy
import pandas as pd
import matplotlib.pyplot as plt
from astropy import io
from scipy.constants import *


def CreateCSV():
	# read the downloaded files
	# ftp://ftp.noao.edu/catalogs/atmospheric_transmission/
	df1 = io.ascii.read('OriginalData/transdata_1_5_mic',names=['Wavenumber','Transmission'])
	df2 = io.ascii.read('OriginalData/transdata_0.5_1_mic', names=['Wavenumber','Transmission'])

	# convert to csvs
	io.ascii.write(df1,'OriginalData/TransData_1_5.csv',overwrite=True)
	io.ascii.write(df2,'OriginalData/TransData_05_1.csv',overwrite=True)

	# download to pandas dataframes. Not efficient but whatever
	LongWave  = pd.read_csv('OriginalData/TransData_1_5.csv',sep=' ')
	ShortWave = pd.read_csv('OriginalData/TransData_05_1.csv',sep=' ')

	# combine into single dataframe with wavelength and frequency
	FULL = pd.concat([LongWave,ShortWave],ignore_index=True)
	FULL['Wavelength'] = [10**4/x for x in FULL['Wavenumber']]
	FULL['Frequency'] = [c/(x*10**-6) for x in FULL['Wavelength']]

	# clip the data between 1 and 0.0
	FULL.loc[FULL['Transmission'] < 0, 'Transmission'] = 0.0
	FULL.loc[FULL['Transmission'] > 1, 'Transmission'] = 1.0

	# save to csv
	FULL.to_csv('ProcessedData/KittPeak.csv',index=False)

	# save to pkl becuase faster
	FULL.to_pickle('ProcessedData/KittPeak.pkl')

	# 'Photometric J and H near-IR Bands'#
def TransmissionPlot(name='Wavelength',RANGE=[0.5,2.5],TITLE='MROI Bandwidth'):

	FULL = pd.read_pickle('ProcessedData/KittPeak.pkl')
	print(FULL)

	if name in list(FULL): # make sure requested name is in columns
		if name == 'Wavelength':
			unit = r'$\mu$m' # units of wavelength
		if name == 'Wavenumber':
			unit = r'cm$^{-1}$' # standard units of wavenumber
			RANGE = [10**4/x for x in (RANGE[1],RANGE[0])]
		if name == 'Frequency':
			unit = 'Hz'
			RANGE = [c/(x*10**-6) for x in (RANGE[1],RANGE[0])]

		NEW = FULL.loc[(FULL[name] >= RANGE[0]) & (FULL[name] <= RANGE[1])]

		fig = plt.figure()
		fig.set_size_inches(14,6)

		plt.plot(NEW[name],NEW['Transmission'],linewidth=0.1,label='Data')

		plt.ylabel('Transmission',fontsize=12)
		plt.xlabel(r'%s [%s]' % (name,unit),fontsize=12)
		plt.xlim((RANGE[0],RANGE[1]))
		plt.title(TITLE,fontsize=14)

		plt.grid(True)
		plt.tight_layout()

	else:
		print('Check Spelling er something.')

TransmissionPlot('Wavelength')

plt.show()

