import pandas as pd
import sqlfun
import math

def drawTCMUR(df_Value,col_names,REG_name,countryOfReg,eventKPI,macro_name,total):
    ##dataframe to array: dfOnlyValue.values
    df = pd.DataFrame(df_Value,columns= col_names,index=pd.MultiIndex.from_product([[REG_name],countryOfReg,eventKPI]))
    df_TCMUR_rate = df.loc[(slice(None),slice(None),['Rate']),:]
    TCMUR_rate = df_TCMUR_rate.iloc[:,-1]
    TCMUR_rate_list = TCMUR_rate.xs("Rate",level=2,axis=0).tolist()
    sqlTCMUR = sqlfun.sql()
    sqlTCMUR.inTCMUR(TCMUR_rate_list, ('20'+df.columns[-1][0:2]), df.columns[-1][4:6], REG_name, countryOfReg, macro_name)
    #region total
    if REG_name == 'APAC':
        if math.isnan(total):
            print(total)
        else:   
            sqlTCMUR.inTCMURTotal(total, ('20'+df.columns[-1][0:2]), df.columns[-1][4:6], REG_name, REG_name, macro_name)

