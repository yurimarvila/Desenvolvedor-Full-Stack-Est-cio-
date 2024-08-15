# Passo 1: Criar o set 'set_inicial' com os valores especificados
set_inicial = {11, 12, 13, 14}

# Imprimir o conteúdo do set
print("Conteúdo do set_inicial:", set_inicial)

# Passo 2: Adicionar o elemento 15 ao set usando add
set_inicial.add(15)

# Imprimir o conteúdo do set
print("Após adicionar 15:", set_inicial)

# Passo 3: Atualizar o set com os elementos 1, 2, 3, 4, 5 usando update
set_inicial.update({1, 2, 3, 4, 5})

# Imprimir o conteúdo do set
print("Após atualizar com {1, 2, 3, 4, 5}:", set_inicial)

# Passo 4: Remover o elemento 13 do set usando discard
set_inicial.discard(13)

# Imprimir o conteúdo do set
print("Após remover 13:", set_inicial)

# Passo 5: Criar um novo set 'novo_set' com os elementos especificados
novo_set = {20, 21, 23, 1, 2}

# Imprimir o conteúdo do novo set
print("Conteúdo do novo_set:", novo_set)

# Passo 6: Realizar operações entre os sets
# União
uniao_sets = set_inicial.union(novo_set)
print("União dos sets:", uniao_sets)

# Interseção
intersecao_sets = set_inicial.intersection(novo_set)
print("Interseção dos sets:", intersecao_sets)

# Diferença
diferenca_sets = set_inicial.difference(novo_set)
print("Diferença entre set_inicial e novo_set:", diferenca_sets)

# Diferença Simétrica
diferenca_simetrica_sets = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre os sets:", diferenca_simetrica_sets)
