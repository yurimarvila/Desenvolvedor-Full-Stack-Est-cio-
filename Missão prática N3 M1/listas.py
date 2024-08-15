lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

print("Conteúdo da lista:", lista_mesclada)

lista_mesclada.append(["Lista aninhada"])


print("Após append:", lista_mesclada)

lista_mesclada.insert(4, 5)

print("Após insert:", lista_mesclada)

print("Tamanho atual da lista:", len(lista_mesclada))

lista_mesclada.pop(1)

print("Após remover item na posição 1:", lista_mesclada)

nova_lista_mesclada = lista_mesclada[:5]

print("Conteúdo da nova lista:", nova_lista_mesclada)