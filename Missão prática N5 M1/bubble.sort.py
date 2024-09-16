# Método bubbleSort que ordena o array
def bubbleSort(array):
    # Primeiro laço for para iterar nos elementos do array
    for i in range(len(array)):
        # Segundo laço for para comparar os elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Comparando os valores adjacentes
            if array[j] > array[j + 1]:
                # Realizando a troca dos valores
                temp = array[j]        # Armazenando o valor atual em uma variável temporária
                array[j] = array[j + 1]  # Substituindo o valor de array[j] por array[j+1]
                array[j + 1] = temp     # Substituindo o valor de array[j+1] pelo valor armazenado na variável temp

# Declaração do array com 15 números
array = [42, 7, 23, 3, 98, 1, 17, 54, 27, 66, 5, 81, 39, 10, 49]

# Aplicando o método bubbleSort no array
bubbleSort(array)

# Imprimindo o array ordenado
print("Array ordenado:", array)