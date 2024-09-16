# Criação do array com números inteiros aleatórios
inteiros = [42, 7, 23, 3, 98, 1, 17, 54, 27, 66, 5, 81, 39, 10, 49]

# Ordenando o array em ordem crescente
inteiros.sort()
print("Array em ordem crescente:", inteiros)

# Ordenando o array em ordem decrescente
inteiros.sort(reverse=True)
print("Array em ordem decrescente:", inteiros)

# Criação do array de strings com os dados: nome, dataNascimento, cpf, rg
pessoas = [
    "Ana;2001-05-14;12345678901;MG1234567",
    "Carlos;1990-12-30;98765432100;SP9876543",
    "Beatriz;1985-07-21;11223344556;RJ2233445",
    "Eduardo;1995-09-10;33445566778;PR3344556",
    "Felipe;1988-11-15;55667788990;RS5566778"
]

# Ordenando o array de strings em ordem alfabética (crescente) pelo nome
pessoas.sort()
print("Array de strings em ordem crescente (pelo nome):")
for pessoa in pessoas:
    print(pessoa)

# Ordenando o array de strings em ordem decrescente pelo nome
pessoas.sort(reverse=True)
print("\nArray de strings em ordem decrescente (pelo nome):")
for pessoa in pessoas:
    print(pessoa)