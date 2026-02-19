from extract import extract
from add_excel import add_excel


def main():
    comprovante = './comprovante.csv'
    sheet_file = './testeautomation.xlsx'
    tab = 'Planilha1'
    
    try:
        df = extract(comprovante)
        add_excel(sheet_file, tab, df)
    except Exception as e:
        print(f"Erro: {e}")
        
if __name__ == "__main__":
    main()