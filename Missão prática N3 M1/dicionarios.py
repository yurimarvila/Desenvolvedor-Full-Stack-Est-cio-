# Criar o dicionário 'meu_dicionario' com os pares de chave/valor especificados
meu_dicionario = {
    1: 'Python',
    2: 'Java',
    3: 'PHP'
}

# Imprimir o conteúdo do dicionário
print("Conteúdo do dicionário 'meu_dicionario':", meu_dicionario)

# Imprimir o tipo de dados do dicionário
print("Tipo de dados de 'meu_dicionario':", type(meu_dicionario))

# Utilizar o método 'get' para obter o valor da chave 'linguagem' para o código 1
valor_linguagem = meu_dicionario.get(1)
print("Valor da chave 'linguagem' para o código 1:", valor_linguagem)

# Imprimir o tamanho do dicionário
tamanho_dicionario = len(meu_dicionario)
print("Tamanho do dicionário 'meu_dicionario':", tamanho_dicionario)

# Criar o dicionário aninhado 'dicionario_frutas'
dicionario_frutas = {
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
}

# Imprimir o valor das chaves 'nome' e 'tipo' da chave 1
print("Nome e Tipo da chave 1:", dicionario_frutas[1]['nome'], '-', dicionario_frutas[1]['tipo'])

# Imprimir o valor das chaves 'nome' e 'tipo' da chave 2
print("Nome e Tipo da chave 2:", dicionario_frutas[2]['nome'], '-', dicionario_frutas[2]['tipo'])

# Utilizar um laço for para iterar no dicionário 'dicionario_frutas' e imprimir todos os valores
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")
