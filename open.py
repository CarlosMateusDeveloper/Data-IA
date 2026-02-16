import pandas as pd

def extract(comprovante):
    df = pd.read_csv(comprovante)
    df = df.drop([3,6,7,8,9,10])
    return df
   
    