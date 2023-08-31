termos_tecnologia = {
    "API": "Interface de Programação de Aplicativos",
    "HTTP": "Protocolo de Transferência de Hipertexto",
    "Github": "Web site"
}


def obter_definicao(palavra):
    return termos_tecnologia.get(palavra, "Palavra não encontrado no dicionário.")


def pesquisar_termo(palavra):
    palavra_pesquisa_lc = palavra.lower()
    palavras_coincidentes = []

    for chave in termos_tecnologia.keys():
        if palavra_pesquisa_lc in chave.lower():
            palavras_coincidentes.append(chave)

    if not palavras_coincidentes:
        return "Nenhuma palavra correspondente encontrado."

    definicoes = []
    for chave in palavras_coincidentes:
        definicao = obter_definicao(chave)
        definicoes.append(f"{chave}: {definicao}")

    return "\n".join(definicoes)
