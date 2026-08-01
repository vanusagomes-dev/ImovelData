"""
analise.py
Real Estate Analytics - Versão com Negrito e Padrão Brasileiro
Autora: Vanusagomes-dev
"""
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

# Defina o nome do arquivo Excel gerado
ARQUIVO = "analise_imoveis.xlsx"

def analisar():
    # Dados atualizados: Imóvel 259k, Aluguel Bruto 2.200, Taxa Adm 150, Líquido 2.050
    dados = {
        "Valor Venda": [259000.0],
        "Aluguel Bruto": [2200.0],
        "Condomínio": [400.0],
        "IPTU": [80.0],
        "Taxa Administração": [150.0],
        "Provisão": [50.0],
        "Aluguel Líquido": [2050.0],
        "Yield Bruto": [0.1019],
        "Yield Líquido": [0.0949],
        "Rentabilidade": [0.07]
    }
    df = pd.DataFrame(dados)
    
    # Salva o DataFrame inicial no Excel
    df.to_excel(ARQUIVO, index=False)
    
    # Aplica a formatação completa
    formatar_excel()

def formatar_excel():
    wb = load_workbook(ARQUIVO)
    ws = wb.active
    azul = "1F4E78"
    
    # Formata o cabeçalho (Linha 1) com fundo azul, texto branco e negrito
    for c in ws[1]:
        c.font = Font(color="FFFFFF", bold=True)
        c.fill = PatternFill("solid", fgColor=azul)
        
    moeda_br = 'R$ #,##0.00_-'
    perc_br = '0,00%'
    
    # Descobre qual coluna é o quê pelo cabeçalho para evitar erros de índice
    header_cells = {cell.value: cell.column - 1 for cell in ws[1]}
    colunas_moeda = ["Valor Venda", "Aluguel Bruto", "Condomínio", "IPTU", "Taxa Administração", "Provisão", "Aluguel Líquido"]
    colunas_perc = ["Yield Bruto", "Yield Líquido", "Rentabilidade"]

    # Percorre todas as linhas de dados a partir da linha 2
    for row in ws.iter_rows(min_row=2):
        for idx, cell in enumerate(row):
            # Aplica negrito em TODAS as células de dados da tabela mantendo a fonte padrão
            current_font = cell.font
            cell.font = Font(name=current_font.name if current_font else 'Calibri', bold=True, size=current_font.size if current_font else 11)
            
        # Formata colunas monetárias pelo nome correto
        for nome_col in colunas_moeda:
            if nome_col in header_cells:
                col_idx = header_cells[nome_col]
                if col_idx < len(row):
                    row[col_idx].number_format = moeda_br
                
        # Formata as colunas em porcentagem pelo nome correto
        for nome_col in colunas_perc:
            if nome_col in header_cells:
                col_idx = header_cells[nome_col]
                if col_idx < len(row) and isinstance(row[col_idx].value, (int, float)):
                    row[col_idx].number_format = perc_br

    # Ajuste automático da largura das colunas
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        w = max(len(str(c.value)) if c.value is not None else 0 for c in col) + 4
        
        if col[0].value and "IPTU" in str(col[0].value):
            w = max(w, 18)
            
        ws.column_dimensions[col_letter].width = w
        
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    wb.save(ARQUIVO)

if __name__ == "__main__":
    analisar()
    