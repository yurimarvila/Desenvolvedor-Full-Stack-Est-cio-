from Calculadora import Calculadora

# Criando uma nova instância da classe Calculadora
calc = Calculadora(10, 5, '+')

# Mostrando o resultado
calc.mostrarResultado()

# Testando outra operação
calc.valorA = 20
calc.valorB = 4
calc.operacao = '/'
calc.mostrarResultado()
