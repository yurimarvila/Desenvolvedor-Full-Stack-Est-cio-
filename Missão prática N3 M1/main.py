from operacoes import calcular_media, verificar_reprovacao, formatar_saida_reprovados

# Dados dos alunos
dados_alunos = {
    26: {'nome': 'Maria', 'notas': [8, 7, 5, 9]},
    101: {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    13: {'nome': 'João', 'notas': [6, 5, 5, 5]},
    37: {'nome': 'Ágatha', 'notas': [8, 6, 7.5, 9]},
    72: {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
    5: {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
}

# Lista para armazenar matrículas de alunos reprovados
matriculas_reprovados = []

# Calcular a média de cada aluno e verificar reprovação
for matricula, dados in dados_alunos.items():
    media = calcular_media(dados['notas'])
    dados['media'] = media
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)

# Identificar e imprimir dados dos alunos reprovados
saidas_reprovados = formatar_saida_reprovados(dados_alunos, matriculas_reprovados)

# Imprimir resultados
for saida in saidas_reprovados:
    print(saida)