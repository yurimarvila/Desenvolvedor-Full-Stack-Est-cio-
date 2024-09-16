# Criação do array com 15 números inteiros aleatórios
array = [42, 7, 23, 3, 98, 1, 17, 54, 27, 66, 5, 81, 39, 10, 49]

# Laço for para iterar nos elementos do array
for i in range(len(array)):
    # Variável que recebe o índice "i"
    min_index = i
    
    # Laço for para iterar a partir da posição i+1 até o final do array
    for j in range(i+1, len(array)):
        # Verifica se o valor do array na posição min_index é maior que o valor na posição j
        if array[min_index] > array[j]:
            min_index = j  # Atualiza min_index com o valor de j

    # Troca os valores do array entre as posições i e min_index
    array[i], array[min_index] = array[min_index], array[i]

# Imprime o array ordenado
print("Array ordenado:", array)