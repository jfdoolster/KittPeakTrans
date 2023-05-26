"""
rewrite
"""

import os
import pandas as pd
from scipy.constants import speed_of_light as c

def read_split_file(file: str, encoding="utf-8", sep=' '):
    """
    creat plain text file
    """
    result=[]
    with open(file,"r", encoding=encoding) as f:
        lines=f.readlines()
        for rawline in lines:
            stripline = rawline.strip()
            splitline = stripline.split(sep)
            finalline = [x for x in splitline if x != '']
            result.append(tuple(finalline))
        f.close()
    return result

def table2dataframe(table: list, columns: list, dtype=None):
    """
    create pickle files from OriginalData
    """
    return pd.DataFrame(table, columns=columns, dtype=dtype)

def calc_wavelength_frequency(df0: pd.DataFrame):
    """
    add wavelength and frequency
    """
    df0['Wavelength [um]'] = 10**4/df0['Wavenumber [1/cm]']
    df0['Frequency [Hz]']  = c/(10**-6 * df0['Wavelength [um]'])

    df0.loc[df0['Transmission'] < 0.0, 'Transmission'] = 0.0
    df0.loc[df0['Transmission'] > 1.0, 'Transmission'] = 1.0

    return df0.sort_values(by='Wavelength [um]')

def proccess_kittpeak_data():
    """
    create dataframes and pkls
    """

    path_pkl_short = os.path.join('data', 'df_short.pkl')
    path_pkl_long = os.path.join('data', 'df_long.pkl')
    path_pkl_full = os.path.join('data', 'df_full.pkl')

    boolgate = True
    if not os.path.exists('data/'):
        boolgate=False
        os.makedirs('data/')
    else:
        boolgate &= (os.path.exists(path_pkl_short))
        boolgate &= (os.path.exists(path_pkl_long))
        boolgate &= (os.path.exists(path_pkl_full))

    if not boolgate:
        tbl_short = read_split_file('original_data/transdata_0.5_1_mic', \
            encoding='ascii', sep=' ')
        tbl_long = read_split_file('original_data/transdata_1_5_mic', \
            encoding='ascii', sep=' ')

        df_short = table2dataframe(tbl_short, dtype=float, \
            columns=['Wavenumber [1/cm]', 'Transmission'])
        df_long  = table2dataframe(tbl_long, dtype=float, \
            columns=['Wavenumber [1/cm]', 'Transmission'])

        df_short = calc_wavelength_frequency(df_short)
        df_long = calc_wavelength_frequency(df_long)

        df_full = pd.concat([df_short, df_long], ignore_index=True)\
            .sort_values(by='Wavelength [um]')

        df_short.to_pickle(path_pkl_short)
        df_long.to_pickle(path_pkl_long)
        df_full.to_pickle(path_pkl_full)

    df_short = pd.read_pickle(path_pkl_short)
    df_long = pd.read_pickle(path_pkl_long)
    df_full = pd.read_pickle(path_pkl_full)

    return df_full, df_long, df_short
