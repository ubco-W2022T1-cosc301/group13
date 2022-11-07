import pandas as pd

def load_and_process(path):
    df1 = (
        pd.read_csv(str(path) + "housing-supply-price-rental.csv")
        .loc[lambda x: x['region']=='vancouver']
        .reset_index(drop=True)
        .loc[:, ['year', 'population', 'region', 'HPI_change', 'CPI_change', 'completed', 'rental', 'total_dwelling', 'employment_change']]
        .astype({'year': int})
        .loc[1:26]
    )
    
    df1['population'] *=1000
    
    df2 = (
        pd.read_csv(str(path) + "vancouver_income_main.csv")
        .set_axis(['year', 'no_of_people', 'people_with_income', 'aggre_income', 'avg_income', 'med_income'], axis=1)
        .loc[:, ['year', 'aggre_income', 'avg_income', 'med_income']]
        .loc[0:25]
    )
    
    df3 = (
        pd.read_csv(str(path) + "hpi_by_region.csv")
        .loc[:, ['year', 'Vancouver, British Columbia']]
        .set_axis(['year', 'total_hpi'], axis=1)
        
    )
    df4 = (df1.merge(df2, how='inner'))
    df5 = (df3.merge(df4, how='inner'))
    
    return df5