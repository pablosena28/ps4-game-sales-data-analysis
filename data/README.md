# Dados

raw/ps4_games_sales.csv contém a base usada no case, normalizada para UTF-8 para facilitar a leitura no GitHub e no Pandas.

O código em src/data_cleaning.py cria variáveis auxiliares sem imputar o ano ausente:

- Sales Recorded: indica se Global > 0;
- Regional Sum: soma das quatro regiões;
- Global Difference: diferença entre Global e a soma regional;
- publisher ausente recebe o rótulo Unknown durante a análise.

A unidade formal das colunas de vendas não está documentada no próprio arquivo.