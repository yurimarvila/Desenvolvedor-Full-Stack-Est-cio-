print("\nEscolha 2 valores para serem somados, subtraídos, multiplicados e divididos!\n")

valor1 = int(input("Digite o primeiro valor que deseja: "))
valor2 = int(input("Digite o segundo valor que deseja: "))

adicao = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

print('\nO resultado da Adição de ' + str(valor1) + ' com ' + str(valor2) + ' é de: ' + str(adicao))
print('\nO resultado da Subtração de ' + str(valor1) + ' com ' + str(valor2) + ' é de: ' + str(subtracao))
print('\nO resultado da Multiplicação de ' + str(valor1) + ' com ' + str(valor2) + ' é de: ' + str(multiplicacao))
print('\nO resultado da Divisão de ' + str(valor1) + ' com ' + str(valor2) + ' é de: ' + str(divisao))

print("\nAdicionei o int nos valores para que seja realizo o calculo de forma correta e não apenas a junção dos numeros.")