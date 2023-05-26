"""
rewrite
"""

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

if __name__ == "__main__":
    tbl_short = read_split_file('OriginalData/transdata_0.5_1_mic', encoding='ascii', sep=' ')
    tbl_long = read_split_file('OriginalData/transdata_1_5_mic', encoding='ascii', sep=' ')

    df_short = table2dataframe(tbl_short, columns=['Wavenumber [1/cm]', 'Transmission'], dtype=float)
    df_long  = table2dataframe(tbl_long, columns=['Wavenumber [1/cm]', 'Transmission'], dtype=float)

    df_short['Wavelength [um]'] = 10**4/df_short['Wavenumber [1/cm]']
    df_short['Frequency [Hz]']  = c/(10**-6 * df_short['Wavelength [um]'])

    df_long['Wavelength [um]'] = 10**4/df_long['Wavenumber [1/cm]']
    df_long['Frequency [Hz]']  = c/(10**-6 * df_long['Wavelength [um]'])

    df_long = df_long.sort_values(by='Wavelength [um]')
    df_short = df_short.sort_values(by='Wavelength [um]')

    df_all = pd.concat([df_short, df_long], ignore_index=True).sort_values(by='Wavelength [um]')

    print(df_all)
    print(df_all.info())
