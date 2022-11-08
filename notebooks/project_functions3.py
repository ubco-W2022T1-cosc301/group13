import pandas as pd
import numpy as np

def load_and_process(path):
        dataSet1 = pd.read_csv(str(path) + "hpi_by_region.csv")
        df1 = ( 
                pd.DataFrame(data=dataSet1,columns=dataSet1.columns).drop(['Atlantic Region', 
                'Ottawa-Gatineau, Ontario part', 'Toronto, Ontario', 'Quebec City, Quebec', 
                'Sherbrooke, Quebec', 'Trois-Rivieres, Quebec', 'Montreal, Quebec', 
                'Ottawa-Gatineau, Quebec part', 'Hamilton, Ontario', 'St. Catharines-Niagara, Ontario', 
                'Kitchener-Cambridge-Waterloo, Ontario', 'Guelph, Ontario', 'London, Ontario', 
                'Windsor, Ontario', 'Greater Sudbury, Ontario 12', 'Prairie Region', 
                'Kelowna, British Columbia', 'Vancouver, British Columbia', 
                'Victoria, British Columbia', 'year', 'month'], axis=1).reset_index(drop=True)
        )

        dataSet2 = pd.read_csv(str(path) + "population-by-region-1946-2022 (1).csv")
        df2 = (
                pd.DataFrame(data=dataSet2,columns=dataSet2.columns)
            .drop(['DGUID', 'VECTOR', 'COORDINATE'], axis=1)
            .iloc[1556]
            .reset_index(drop=True)
        )
        
        df3 = df1.join(df2, lsuffix='_l', rsuffix='_r')
        
        return df3
