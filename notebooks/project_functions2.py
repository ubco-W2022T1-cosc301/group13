import pandas as pd

def load_and_process(path):
    dataset_population_by_region = (
        pd.read_csv(str(path) + 'population-by-region-1946-2022 (1).csv')
        .loc[lambda x: x['GEO']=='British Columbia']
        .reset_index(drop=True)
        .loc[:, ['REF_DATE', 'GEO', 'Population estimate']]
        .set_axis(['Year', 'Province', 'Population'], axis='columns')
        .iloc[-80:]
    )
    dataset_population_by_region['Year'] = pd.DatetimeIndex(pd.to_datetime(dataset_population_by_region['Year'], format='%b-%y')).year
   
    dataset_hpi_by_region = (
        pd.read_csv(str(path) + 'hpi_by_region.csv')
        .reset_index(drop=True)
        .loc[:, ['Type', 'British Columbia ', 'year']]
        .set_axis(['Type', 'BC-HPI', 'Year'], axis='columns')
        .iloc[-740:-498]
    )
    
    dataset_vacancy_rate = (
        pd.read_csv(str(path) + 'housing-supply-and-rental/british columbia_section1_.csv')
        .reset_index(drop=True)
        .loc[:, ['Unnamed: 0', 'Rental vacancy rate (%)3']]
        .set_axis(['Year', 'Vacancy Rate(%)'], axis='columns')
        .iloc[-17:-2]
    )
    
    final_data1 = (dataset_population_by_region.merge(dataset_hpi_by_region, how='inner'))
    final_data2 =
    
    return final_data2
    
 
    