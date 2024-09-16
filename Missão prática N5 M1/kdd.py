import time

# Função Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Função Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# Lendo o conteúdo do arquivo e separando as palavras
with open('texto.txt', 'r') as arquivo:
    palavras = list()
    for linha in arquivo:
        palavras.extend(linha.split())  # Quebrando as linhas em palavras e adicionando à lista

# Ordenação com Bubble Sort e medição de tempo
palavras_bubble = palavras.copy()
inicio_bubble = time.time()
bubble_sort(palavras_bubble)
fim_bubble = time.time()
print("\nOrdenação Bubble Sort:")
print(palavras_bubble)
print(f"Tempo de execução (Bubble Sort): {fim_bubble - inicio_bubble} segundos")

# Ordenação com Selection Sort e medição de tempo
palavras_selection = palavras.copy()
inicio_selection = time.time()
selection_sort(palavras_selection)
fim_selection = time.time()
print("\nOrdenação Selection Sort:")
print(palavras_selection)
print(f"Tempo de execução (Selection Sort): {fim_selection - inicio_selection} segundos")

# Ordenação com método nativo sort() e medição de tempo
palavras_sort = palavras.copy()
inicio_sort = time.time()
palavras_sort.sort()
fim_sort = time.time()
print("\nOrdenação com método nativo sort:")
print(palavras_sort)
print(f"Tempo de execução (sort): {fim_sort - inicio_sort} segundos")

# Salvando o resultado da ordenação com o método escolhido (sort) em um novo arquivo
with open('palavras_ordenadas.txt', 'w') as arquivo_saida:
    arquivo_saida.write(' '.join(palavras_sort))

print("\nPalavras ordenadas salvas no arquivo 'palavras_ordenadas.txt'.")