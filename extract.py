import pandas as pd

def extract(comprovante):
    df = pd.read_csv(comprovante)
    df = df.loc[:,['Valor','Data' ,'Hora', 'Nome', 'Tipo de Transferencia'] ]
    return df
   

   
    