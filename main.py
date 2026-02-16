from open import extract
from add_sheet import add_sheet


def main():
    comprovante = './comprovante.csv'
    sheet_file = './planilha.xlsx'
    tab = 'Sheet1'
    
    try:
        extract(comprovante)
        add_sheet(sheet_file, tab, comprovante)
    except Exception as e:
        print(f"Erro: {e}")
        
if __name__ == "__main__":
    main()