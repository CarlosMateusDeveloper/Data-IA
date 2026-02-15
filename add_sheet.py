from open import extract
import pandas as pd
from openpyxl import Workbook, load_workbook

def add_sheet( sheet_file):
    df = extract()
    book = load_workbook(sheet_file)
    ws = book['planilha1']
    
    for i in df.values:
        ws.append(i)
    
    book.save(sheet_file)