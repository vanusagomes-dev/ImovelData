# 📊 Análise de Imóveis - Automação de Relatórios Financeiros

> **Python | Pandas | OpenPyXL | SQLite | Excel | Git | GitHub | Data Analytics**

Sistema desenvolvido em **Python** para análise de rentabilidade imobiliária, geração automática de relatórios financeiros e exportação estruturada dos dados para Excel.

O projeto tem como objetivo auxiliar na avaliação de oportunidades imobiliárias por meio do cálculo de indicadores financeiros como **Yield Bruto, Yield Líquido e Rentabilidade**, proporcionando uma visão mais clara para a tomada de decisão de investimentos.

---

# 🚀 Funcionalidades do Projeto

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

```text
projeto-data-analytics/
│
├── Analise_Imoveis.xlsx
│
├── images/
│   └── Analise_Imoveis.jpeg
│
├── notebooks/                 # Testes futuros e análises exploratórias
│
├── .gitignore                 # Arquivos temporários ignorados pelo Git
│
├── analise.py
│
├── database.py
│
├── README.md
│
├── LICENSE
│
└── data/                      # Base de dados do projeto
    └── imoveis.db
```

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- OpenPyXL
- SQLite
- Microsoft Excel
- Git
- GitHub
- Visual Studio Code

---

# 📌 Regras de Negócio Aplicadas

## Taxa Administrativa

Considera uma taxa de administração aplicada sobre a receita de aluguel.

## Provisão de Custos

Considera valores destinados à manutenção e demais despesas relacionadas ao imóvel.

## Indicadores Financeiros

### Yield Bruto

Mede o retorno anual do aluguel bruto em relação ao valor investido no imóvel.

### Yield Líquido

Representa o retorno anual considerando todos os custos e despesas envolvidos.

### Rentabilidade

Indicador utilizado para demonstrar o potencial de retorno do investimento imobiliário.

---

# ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Vanusagomes-dev/projeto-data-analytics.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd projeto-data-analytics
```

### 3️⃣ Instale as dependências

```bash
pip install pandas openpyxl
```

### 4️⃣ Execute o sistema

```bash
python analise.py
```

---

# 📈 Saída do Projeto

Após executar o programa:

- O relatório será exibido diretamente no terminal do VS Code;
- Será gerada automaticamente a planilha:

```text
Analise_Imoveis.xlsx
```

A planilha conterá todos os indicadores financeiros formatados e organizados para análise.

Em computadores com Microsoft Excel instalado, o arquivo será aberto automaticamente após a execução do sistema.

---

# 🖼️ Prévia do Relatório

Abaixo está um exemplo da planilha gerada automaticamente pelo sistema.

![Relatório Excel](images/Analise_Imoveis.jpeg)

---

# 📊 Exemplo de Indicadores Gerados

| Indicador | Resultado |
|-----------|----------:|
| Valor do imóvel | R$ 259.000,00 |
| Aluguel bruto | R$ 2.200,00 |
| Taxa Administração | R$ 150,00 |
| Aluguel líquido | R$ 2.050,00 |
| Yield Bruto | 10,19% |
| Yield Líquido | 9,49% |
| Rentabilidade | 7,00% |

---

# 🎯 Objetivo Profissional

Este projeto faz parte do meu portfólio em **Data Analytics**, demonstrando a aplicação prática de:

- Automação de relatórios;
- Tratamento e organização de dados;
- Análise financeira;
- Geração de indicadores;
- Python aplicado a negócios.

A solução foi desenvolvida para simular um cenário real de análise financeira imobiliária, aplicando automação, organização de dados e geração de indicadores para apoiar a tomada de decisão de investidores e profissionais do mercado imobiliário.

# 👩‍💻 Desenvolvido por

**Vanusa Pereira Gomes**

GitHub:

https://github.com/Vanusagomes-dev

Projeto desenvolvido para estudos e aplicação prática de **Python, Data Analytics e Inteligência de Negócios**.
