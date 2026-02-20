from extract import extract
from add_excel import add_excel
from pathlib import Path


def main():
    comprovante = './comprovante.csv'
    sheet_file = Path(r'C:\Users\carlo\OneDrive\Documentos\Testepython2.xlsx')
    tab = 'Planilha1'
        
    try:
        df = extract(comprovante)
        add_excel(sheet_file, tab, df)
    except Exception as e:
        print(f"Erro: {e}")
        
if __name__ == "__main__":
    main()