import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
from astropy.io import ascii
from scipy.constants import *


def CreateCSV():
	# read the downloaded files
	# ftp://ftp.noao.edu/catalogs/atmospheric_transmission/
	df1 = ascii.read('OriginalData/transdata_1_5_mic',names=['Wavenumber','Transmission'])
	df2 = ascii.read('OriginalData/transdata_0.5_1_mic', names=['Wavenumber','Transmission'])

	# convert to csvs
	ascii.write(df1,'OriginalData/TransData_1_5.csv',overwrite=True)
	ascii.write(df2,'OriginalData/TransData_05_1.csv',overwrite=True)

	# download to pandas dataframes. Not efficient but whatever
	LongWave  = pd.read_csv('TransData_1_5.csv',sep=' ')
	ShortWave = pd.read_csv('TransData_05_1.csv',sep=' ')

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
	FULL.to_pkl('ProcessedData/KittPeak.pkl')
CreateCSV()

# 'Photometric J and H near-IR Bands'#
def PlotEm(name='Wavelength',RANGE=[1.2,1.8],TIT='PARVI Bandwidth'):

	# pull pkl dataset
	FULL = pd.read_pkl('ProcessedData/KittPeak.pkl')

	if name in list(FULL):
		if name == 'Wavelength':
			unit = r'$\mu$m'
		if name == 'Wavenumber':
			unit = r'cm$^{-1}$'
			RANGE = [10**4/x for x in (RANGE[1],RANGE[0]) ]
		if name == 'Frequency':
			unit = 'Hz'
			RANGE = [c/(x*10**-6) for x in (RANGE[1],RANGE[0]) ]

		NEW = FULL.loc[(FULL[name] >= RANGE[0]) & (FULL[name] <= RANGE[1])]

		fig = plt.figure()
		fig.set_size_inches = (12,8)

		plt.plot(NEW[name],NEW['Transmission'],linewidth=0.3)

		plt.ylabel('Transmission',fontsize=14)
		plt.xlabel(r'%s [%s]' % (name,unit),fontsize=14)
		plt.title(TIT,fontsize=20)

		plt.grid(True)
		plt.tight_layout()

		if True:
			deg  = 2
			beta = np.polyfit(NEW[name],NEW['Transmission'],deg)
			yhat = []
			for x in NEW[name]:
				hat  = 0
				order = copy.deepcopy(deg)
				for d in range(deg):
					print(d)
					print(order,'\n')
					hat += beta[d] * x ** order
					order -= 1
					quit()
				yhat.append(hat)

			plt.plot(NEW[name],yhat)


	else:
		print('Check Spelling er something.')

PlotEm('Wavelength',RANGE=[0.9,2.5],TIT='Near-IR')
#PlotEm('Wavelength',RANGE=[0.5,0.8],TIT='Visible')

plt.show()

