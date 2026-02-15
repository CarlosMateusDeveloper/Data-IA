
import pandas as pd


# wb = load_workbook()         
# ws = wb.active 


def extract(comprovante, sheet):
    df = pd.read_csv(comprovante)
   
        