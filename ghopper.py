def resumo():
    mensagem = "Grace Murray Hopper (Nova Iorque, 9 de dezembro de 1906 — Condado de Arlington, 1 de janeiro de 1992) foi almirante e analista de sistemas da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic (em desuso) — base para a criação do COBOL — e uma das primeiras programadoras do computador Harvard Mark I[1] em 1944. "
    return mensagem


def doutorado():
    mensagem = "matematica e fisica, doutorado em matematica"
    return mensagem


def contribuicoes():
    mensagem = "criou a linuagem do kobol"
    return mensagem


def artigos():
    mensagem = "HOPPER, Grace Murray. Grace Hopper. 1979.\nWILLIAMS, Kathleen Broome. Grace Hopper: Admiral of the cyber sea. Naval Institute Press, 2013."
    return mensagem


def citacoes():
    mensagem = "Para mim programação é mais do que uma arte prática importante. É também um empreendimento gigantesco nos fundamentos do conhecimento."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
