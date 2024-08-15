# Criar o dicionário inicial
dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

# Adicionar novos elementos ao dicionário usando o método 'update'
dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})

# Imprimir o dicionário atualizado
print("Dicionário após o update:", dicionario)

# Criar uma cópia do dicionário usando o método 'copy'
dicionario_copia = dicionario.copy()

# Remover um elemento do primeiro dicionário usando o método 'pop'
elemento_removido = dicionario.pop(2)

# Imprimir o dicionário após remover o elemento
print("Dicionário após o pop:", dicionario)

# Imprimir o elemento removido
print("Elemento removido:", elemento_removido)

# Remover o último elemento do dicionário usando o método 'popitem'
elemento_removido_popitem = dicionario.popitem()

# Imprimir o dicionário após remover o último elemento
print("Dicionário após o popitem:", dicionario)

# Imprimir o elemento removido com 'popitem'
print("Último elemento removido com popitem:", elemento_removido_popitem)

# Remover todos os elementos dos dicionários usando o método 'clear'
dicionario.clear()
dicionario_copia.clear()

# Imprimir os dicionários após serem esvaziados
print("Dicionário após o clear:", dicionario)
print("Cópia do dicionário após o clear:", dicionario_copia)

# Criar um novo dicionário usando o método 'fromKeys'
chaves = [1, 2, 3, 4, 5]
novo_dicionario = dict.fromkeys(chaves, "Valor Padrão")

# Imprimir o conteúdo do novo dicionário usando o método 'items'
print("Novo dicionário (items):", list(novo_dicionario.items()))

# Imprimir apenas as chaves do novo dicionário usando o método 'keys'
print("Chaves do novo dicionário (keys):", list(novo_dicionario.keys()))

# Imprimir apenas os valores do novo dicionário usando o método 'values'
print("Valores do novo dicionário (values):", list(novo_dicionario.values()))
