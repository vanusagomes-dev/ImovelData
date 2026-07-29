# Importando as bibliotecas principais para Data Analytics
import pandas as pd
import numpy as np

print("Ambiente de Data Analytics configurado com sucesso!")

# Exemplo de carregamento de dados (substitua pelo caminho do seu arquivo CSV ou Excel quando tiver)
# df = pd.read_excel('seu_arquivo.xlsx')
#print(df.head())

#===============================================
#Sistema ImóvelData - Cálculo de Rentabilidade#
#===============================================

def analisar_imovel(nome_imovel, valor_venda, aluguel_mensal):
    # Calcula a receita anual de aluguel
    aluguel_anual = aluguel_mensal * 12

    # Calcula a porcentagem do retorno ao ano (vield)
    rentabilidade_anual = (aluguel_anual / valor_venda) * 100


    print(f"\n--- Análise do Imóvel: {nome_imovel} ---")
    print(f"Valor do Imóvel: R$ {valor_venda:,.2f}")
    print(f"Aluguel Mensal: R$ {aluguel_mensal:,.2f}")
    print(f"Rentabilidade Anual: {rentabilidade_anual:.2f}% ao ano")

    # Classificação simples de negócio
    if rentabilidade_anual >= 6.0:
       print("Resultado: EXCELENTE Oportunidade de investimento!")
    else:
        print("Resultado: Rentabilidade abaixo da média do mercado.")

# Testando o programa com um exemplo prático:
if __name__ == "__main__":
    analisar_imovel("Studio Centro SP", 259000, 2200)

