from pyxlsb import open_workbook as open_xlsb
import pandas as pd
import macro
import process
import sqlfun

'''
goal: I wanna get lastest week rate to insert into database.
'''
def extract(macro_module):
    df = []
    #read xlsb
    with open_xlsb('./test/TCMUR.xlsb') as wb:
        with wb.get_sheet(1) as sheet:
            for row in sheet.rows():
                df.append([item.v for item in row])
    #get week list
    wk_list = []
    for y in range(len(df[1])):
        if df[13][y] is not None and df[13][y] != 'REGION' and df[13][y] != 'COUNTRY' and df[13][y] != 'CENTER' and df[13][y] != 'KPI':
             wk_list.append(df[13][y])

    #transfer list to dataframe
    df = (pd.DataFrame(df[14:], columns=df[13]))

    #drop row and column where are all NaN data
    df.dropna(axis=0, how='all',inplace=True)
    df.dropna(axis=1, how='all',inplace=True)

    #extract value of area
    dfOnlyValue = df.iloc[:,3:]
    apac = df['REGION'].values.tolist().index('APAC Rate')
    df_Value_APAC = dfOnlyValue[:apac]
    
    #extract country
    apac_country = []
    for i in range(len(df['COUNTRY'])):
        if df['COUNTRY'][i] is not None and i < apac:
            apac_country.append(df['COUNTRY'][i])

    #deal with problem of string
    for j in range(len(apac_country)):
        if apac_country[j] == "CEETE B'IVRRE":
            apac_country[j] =  'CEETE B\"IVRRE'

    #items   
    kpi = ['Rate','U Qty','C Qty','Target']

    #Region total rate
    apac_total = df.iloc[:,-1:][apac:apac+1].values.tolist()[0][0]

    #insert APAC's Rate to mysql
    process.drawTCMUR(df_Value_APAC.values,wk_list,'APAC',apac_country,kpi,macro_module,apac_total)           


if __name__ == '__main__':
    macro.changeMacro('HH','TCMUR.xlsb')
    extract(1)
    macro.changeMacro('NB','TCMUR.xlsb')
    extract(0)    
