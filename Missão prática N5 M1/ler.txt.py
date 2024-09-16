# Abrindo e lendo o arquivo com o método open
arquivo = open('loremipsum.txt', 'r')

# Imprimindo o conteúdo completo do arquivo
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:\n", conteudo)

# Voltando ao início do arquivo para ler novamente
arquivo.seek(0)  # Retorna o ponteiro do arquivo ao início

# Imprimindo apenas a primeira linha do arquivo
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:\n", primeira_linha)

# Voltando ao início do arquivo novamente
arquivo.seek(0)

# Imprimindo os 3 primeiros caracteres do arquivo
tres_primeiros = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:\n", tres_primeiros)

# Fechando o arquivo após a leitura
arquivo.close()

# Utilizando a instrução "with" para abrir e ler o arquivo
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()
    print("\nConteúdo lido com 'with':\n", conteudo_with)