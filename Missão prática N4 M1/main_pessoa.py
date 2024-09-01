from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Crie uma instância da classe Pessoa
pessoa1 = Pessoa("João", "12345", "2024-01-01", False)
pessoa1.print_attributes()

# Crie uma instância da classe PessoaFisica
pessoa_fisica = PessoaFisica("Ana", "67890", "2022-01-01", False, "2000-01-01", "000.111.222-33", "15975388-1")
pessoa_fisica.print_attributes()

# Crie uma instância da classe PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa X", "54321", "2023-01-01", False, "2020-05-05", "00.000.000/0001-00")
pessoa_juridica.print_attributes()

# Modifique os atributos usando os setters
pessoa1.nome = "Carlos"
pessoa_fisica.nome = "Beatriz"
pessoa_juridica.nome = "Empresa Y"

# Tente definir um CPF inválido (menos de 14 caracteres)
try:
    pessoa_fisica.cpf = "123.456.789-0"  # Deve gerar um ValueError
except ValueError as e:
    print(f"Erro ao definir CPF: {e}")

# Tente definir um CNPJ inválido (menos de 18 caracteres)
try:
    pessoa_juridica.cnpj = "12.345.678/0001-0"  # Deve gerar um ValueError
except ValueError as e:
    print(f"Erro ao definir CNPJ: {e}")

# Imprima os valores atualizados
pessoa1.print_attributes()
pessoa_fisica.print_attributes()
pessoa_juridica.print_attributes()
