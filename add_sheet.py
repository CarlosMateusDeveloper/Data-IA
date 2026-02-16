from open import extract
import pandas as pd
from openpyxl import Workbook, load_workbook

def add_sheet( sheet_file, tab, comprovante):
    df = extract(comprovante)
    book = load_workbook(sheet_file)
    ws = book[tab]
    
    for i in df.values:
        ws.append(i)
    
    book.save(sheet_file)