# Qualidade dos dados

A base possui **1.034 registros** e **9 colunas**.

## Problemas identificados

- 209 registros sem Year;
- 209 registros sem Publisher;
- os 209 casos de ano ausente coincidem com os 209 casos de publisher ausente;
- 322 registros possuem Global = 0;
- não há duplicatas completas;
- há 3 nomes de jogos repetidos com metadados diferentes;
- todos os registros de 2019 e 2020 possuem venda global zero no arquivo fornecido.

## Decisões metodológicas

### Ano e publisher ausentes

O projeto não imputa o ano. Publisher ausente recebe apenas o rótulo Unknown durante a preparação para permitir agrupamentos.

### Vendas iguais a zero

Os registros com venda zero permanecem na base. Eles não são tratados automaticamente como fracasso comercial.

### Janela temporal

A análise de tendência utiliza **2013–2018**. Os anos de 2019 e 2020 são excluídos da interpretação temporal principal porque todos os seus registros possuem vendas globais iguais a zero.

### Nomes repetidos

Apotheon, Biomutant e War Thunder aparecem mais de uma vez com metadados distintos. Os registros não são removidos automaticamente.

### Publishers relacionados

Rótulos como Electronic Arts e EA Sports, além de nomes distintos da Sony, são preservados como aparecem na fonte.

## Unidade das vendas

O CSV não traz um dicionário de dados com a unidade formal das colunas de vendas. Por isso, o projeto usa a expressão **“unidade do dataset”**.