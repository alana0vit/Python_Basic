# importando o módulo tabulate da biblioteca tabulate e o módulo Pandas
from tabulate import tabulate
import pandas

# uma lista
lista = [
    ["Produto", "Preço", "Qtde"],
    ["Iphone", 6000, 50],
    ["Ipad", 10000, 15],
    ["Airpod", 2000, 100]
]

# um dicionário
dic_produtos = {
    "Produto":["Iphone", "Ipad", "Airpod"],
    "Preço": [6000, 10000, 2000],
    "Qtde": [50, 15, 100]
}

# imprimindo a lista para ver como é mostrado normalmente pelo terminal
print(lista)

# imprimindo a tabela baseado na lista, definindo o cabeçalho como a primeira linha(firstrow)...;
# e o formato da tabela com o table format, existe vários formatos, fancy_grid e github são exemplos. Há também o html, que fornece não um formato, mas um código para
# ser lançado num arquivo .html e mostrar a tabela na web
print(tabulate(lista, headers="firstrow", tablefmt="fancy_grid"))

# imprimindo o dicionário para ver como é mostrado normalmente pelo terminal
print(dic_produtos)

# imprimindo a tabela baseado no dicionário, definindo o cabeçalho com as chaves do dicionário e seguindo o mesmo padrão de formato.
# tanto dicionários, quanto tabelas importadas pelo módulo Pandas, tem de se colocar o argumento "keys" no parâmetro "headers".
print(tabulate(dic_produtos, headers="keys", tablefmt="fancy_grid"))

# Vale ressaltar que não é aconselhável usar tabelas importadas pelo Pandas no tabulate, dependendo do tamanho, terá grande dificuldade de letuira da tabela
# uma opção para esse problema é criar um arquivo .html com a tabela importada para que ela possa ser vista no navegador
tabela = pandas.read_csv("base.csv") # importando a tabela com Pandas
tabela.to_html("tabela.html") # transformando em uma extensão .html