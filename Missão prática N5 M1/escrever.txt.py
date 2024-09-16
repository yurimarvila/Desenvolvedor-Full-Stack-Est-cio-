# Abrindo (ou criando) o arquivo "texto.txt" no modo de escrita
arquivo = open('texto.txt', 'w')

# Criando uma lista vazia
texto = list()

# Utilizando o método append para adicionar frases à lista
texto.append("Primeira frase adicionada ao arquivo.\n")
texto.append("Segunda frase adicionada ao arquivo.\n")
texto.append("Terceira frase adicionada ao arquivo.\n")

# Escrevendo o conteúdo da lista no arquivo
arquivo.writelines(texto)

# Fechando o arquivo após a escrita
arquivo.close()

print("Conteúdo escrito no arquivo texto.txt com sucesso!")