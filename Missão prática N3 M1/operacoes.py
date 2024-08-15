# operacoes.py

def calcular_media(notas):
    """
    Calcula a média das notas dos 4 bimestres.
    :param notas: Lista contendo as notas dos 4 bimestres.
    :return: Média das notas.
    """
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se o aluno foi reprovado.
    :param media: Média das notas do aluno.
    :return: True se a média for inferior a 6, False caso contrário.
    """
    return media < 6

def formatar_saida_reprovados(dados_alunos, matriculas_reprovados):
    """
    Formata a saída para alunos reprovados.
    :param dados_alunos: Dicionário contendo nome e matrícula dos alunos.
    :param matriculas_reprovados: Lista das matrículas dos alunos reprovados.
    :return: Lista de strings formatadas com informações dos alunos reprovados.
    """
    saidas = []
    for matricula in matriculas_reprovados:
        if matricula in dados_alunos:
            nome = dados_alunos[matricula]['nome']
            media_final = dados_alunos[matricula]['media']
            saida = f"Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media_final:.2f}"
            saidas.append(saida)
    return saidas
