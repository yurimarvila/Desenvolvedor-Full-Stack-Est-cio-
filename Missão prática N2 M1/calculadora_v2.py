saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return a / b

def calculadora(nun1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(nun1, num2)

    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(nun1, num2)
    
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(nun1, num2)

    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(nun1, num2)

    else:
        return "Operação Inválida"
    
    return resultado

while saida.lower() != 'n':
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação matemática desejada (+, -, *, /) ou o nome da operação (adicao, subtracao, multiplicacao, divisao): ")

    resultado = calculadora(primeiro_numero, segundo_numero, operacao)

    print ("Resultado da operação:", resultado)

    saida = input("Deseja continuar? (S/N): ")