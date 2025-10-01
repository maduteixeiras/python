import os
os.system("cls")


#SAÍDA DE DADOS 
# print pulando linha
print("texto")
# print na mesma linha 
print("texto " , end='')

# f- string + print()
print(f"preço do produto {25.87543: .2f}")


# sempre entre  {} e coloca o : antes da formatação e f antes das ""
#formatadores de STR : 

# {dado: <tam} = formata para esquerda
# {dado: >tam} = formata para direita
# {dado: ^tam} = no max de acordo com o tamanho

# exemplo
conteudo = "teste"
print(f"formatação para a esquerda {conteudo: <16}")
#####


#formatadores de INT :
# {dado: d} = decimal(base 10) usa no dia a dia 
# {dado: x} = hexadecimal usa no css e html, espaços em mémoria e hashes
# {dado: o} = octal uso em linux
# {dado: b} = binario usa em eletronica digital

#exemplos: 
dado = 10

print(f"Decimal     : {dado:d}")
print(f"Hexadecimal : {dado:x}")  # minúsculo
print(f"Hexadecimal : {dado:X}")  # maiúsculo
print(f"Octal       : {dado:o}")
print(f"Binário     : {dado:b}")

#formatação de FLOAT : 
#{dado: tamf} = para declarar quantos num apos a , atraves do tam
#{dado: e} = notação cientifica
#{dado: .tame} = notação cientifica e escolhendo quant de num após a ,

#formatação de DATA E TEMPO : 
#{dado : %Y-%m-%d} = ano - mes - dia
#{dado: %H-%M-%S} = hora - minuto = segundo

# caracteres de escape ;

# barra invertida = \\
# aspas = \"
# pula linha = \n
# tab = \t 
# teb vertical = \v
# apagar(backspace) = \b 
