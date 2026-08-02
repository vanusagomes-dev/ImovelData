# 📊 Análise de Imóveis - Automação de Relatórios Financeiros

Sistema desenvolvido em *Python* para análise de rentabilidade imobiliária, geração automática de relatórios financeiros e exportação estruturada dos dados para Excel.

O projeto tem como objetivo auxiliar na avaliação de oportunidades imobiliárias através do cálculo de indicadores financeiros como *Yield Bruto, Yield Líquido e Rentabilidade*, proporcionando uma visão mais clara para tomada de decisão de investimento.

---

## 🚀 Funcionalidades do Projeto

✅ Processamento automático de dados imobiliários utilizando Python.

✅ Cálculo de indicadores financeiros:

- Valor de venda do imóvel;
- Receita de aluguel bruto;
- Custos operacionais;
- Taxa administrativa;
- Provisão para despesas;
- Aluguel líquido;
- Yield Bruto;
- Yield Líquido;
- Rentabilidade.

✅ Geração automática de relatório em Excel.

✅ Formatação profissional da planilha:

- Cabeçalho personalizado;
- Cores e destaques visuais;
- Valores monetários em Real (R$);
- Percentuais formatados;
- Colunas ajustadas automaticamente;
- Filtro de dados;
- Congelamento do cabeçalho.

✅ Visualização do relatório diretamente no terminal do VS Code.

✅ Abertura automática da planilha Excel após a execução.

---

# 🏗️ Estrutura do Projeto

text
projeto-data-analytics/
│
├── Analise_Imoveis.xlsx        # Relatório financeiro gerado automaticamente
│
│── images/
│   └── Analise_Imoveis.jpeg    # Imagem da planilha
│── noteboks
│
│──.gitgnore                   
│
├── analise.py                 # Código principal de análise e geração do relatório
│
├── README.md                  # Documentação do projeto
│
│── LICENSE                    # MIT
│
│── database.py                # Banco de dados SQLite (estrutura futura)
│
└── data/
    └── imoveis.db             

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- OpenPyXL
- Excel
- SQLite (estrutura preparada para evolução)

---

# 📌 Regras de Negócio Aplicadas

## Taxa Administrativa

Considera uma taxa de administração sobre a receita de aluguel.

## Provisão de Custos

Considera valores destinados para manutenção e despesas relacionadas ao imóvel.

## Indicadores Financeiros

### Yield Bruto

Mede o retorno anual do aluguel bruto em relação ao valor investido no imóvel.

### Yield Líquido

Representa o retorno anual considerando os descontos e custos envolvidos.

### Rentabilidade

Indicador utilizado para demonstrar o potencial de retorno do investimento imobiliário.

---

# ▶️ Como Executar o Projeto

Clone o repositório:

bash
git clone https://github.com/Vanusagomes-dev


Acesse a pasta do projeto:

bash
cd projeto-data-analytics


Instale as dependências:

bash
pip install pandas openpyxl


Execute o sistema:

bash
python analise.py

---

# 📈 Saída do Projeto

Após executar o programa:

- O relatório será exibido no terminal do VS Code;
- Será criada automaticamente a planilha:


Analise_Imoveis.xlsx


A planilha conterá os indicadores financeiros formatados e organizados para análise.

Em computadores com Microsoft Excel instalado, o arquivo será aberto automaticamente após a execução.

---

# 📊 Exemplo de Indicadores Gerados

| Indicador | Resultado |
|---|---:|
| Valor do imóvel | R$ 259.000,00 |
| Aluguel bruto | R$ 2.200,00 |
| Taxa Administração | R$ 150,00 |
| Aluguel líquido | R$ 2.050,00 |
| Yield Bruto | 10,19% |
| Yield Líquido | 9,49% |
| Rentabilidade | 7,00% |

---

# 🎯 Objetivo Profissional

Este projeto faz parte do meu portfólio em *Data Analytics*, demonstrando aplicação prática de:

- Automação de relatórios;
- Tratamento e organização de dados;
- Análise financeira;
- Geração de indicadores;
- Python aplicado a negócios.

A solução foi desenvolvida pensando em cenários reais do mercado imobiliário, auxiliando investidores e profissionais na análise de oportunidades.

---

# 👩‍💻 Desenvolvido por

*Vanusa Gomes*

GitHub:
*Vanusagomes-dev*

Projeto desenvolvido para estudos e aplicação prática de *Python, Data Analytics e Inteligência de Negócios.*

# 📄 Licença

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo [LICENSE](LICENSE) para mais informaçõe


















































