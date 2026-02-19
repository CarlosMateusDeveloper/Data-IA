from openpyxl import Workbook, load_workbook


def add_excel( sheet_file, tab, df):
    book = load_workbook(sheet_file)
    ws = book[tab]
    for row in df.itertuples(index=False):
        ws.append(tuple(row))

    book.save(sheet_file)