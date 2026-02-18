import pandas as pd

comprovante = './comprovante.csv'

def extract(comprovante):
    df = pd.read_csv(comprovante, header=None)
    df = df.set_index(0).T
    df = df.loc[:,['Data','Hora','Valor', 'Tipo de Transferencia', 'Nome'] ]
    return df
   

   
    