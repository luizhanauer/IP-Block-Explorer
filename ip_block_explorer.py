import requests
from tabulate import tabulate

# Faz o download do arquivo
url = "https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest"
response = requests.get(url)
conteudo = response.text
# Salva o conteúdo do arquivo em um arquivo local
with open("delegated-lacnic-extended-latest.txt", "w") as f:
    f.write(conteudo)

print("""
██╗██████╗     ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗    ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║██████╔╝    ██████╔╝██║     ██║   ██║██║     █████╔╝     █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝
██║██╔═══╝     ██╔══██╗██║     ██║   ██║██║     ██╔═██╗     ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
██║██║         ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝╚═╝         ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
by Luiz Hanauer
""")

while True:

    # Solicita o valor a ser pesquisado
    valor_pesquisa = input("Digite o ASN que deseja pesquisar os blocos (ou 'q' para sair): ")
    print()

    # Verifica se o usuário digitou 'q' para sair
    if valor_pesquisa.lower() == 'q':
        break

    # Abre o arquivo
    with open("delegated-lacnic-extended-latest.txt", "r") as f:
        linhas = f.readlines()

    # Valida as linhas e remove as inválidas
    linhas_validas = []
    for linha in linhas:
        parametros = linha.strip().split("|")
        if len(parametros) == 8:
            linhas_validas.append(parametros)

    # Busca os registros de acordo com a pesquisa
    registros_pesquisa = []
    valor_pesquisa_encontrado = False
    valor_pesquisa_oitavo_parametro = None

    # Itera pelas linhas válidas e busca o valor pesquisado e o valor do oitavo parâmetro
    for parametros in linhas_validas:
        if parametros[2] == "asn" and parametros[3] == valor_pesquisa:
            valor_pesquisa_oitavo_parametro = parametros[7]
            valor_pesquisa_encontrado = True

    # Itera novamente pelas linhas válidas e adiciona os registros correspondentes aos critérios de pesquisa
    for parametros in linhas_validas:
        if parametros[2] in ["ipv4", "ipv6"]:
            if valor_pesquisa_encontrado and parametros[7] == valor_pesquisa_oitavo_parametro:
                registros_pesquisa.append(parametros)
            elif not valor_pesquisa_encontrado:
                print("Valor de pesquisa não encontrado em nenhum registro do tipo ASN.")
                print()
                break

    # Imprime os resultados, se houver
    if valor_pesquisa_encontrado == True:
        headers = ['Registry', 'CC', 'Type', 'Start Address', 'Value', 'Date', 'Status', 'Opaque ID']
        print(tabulate(registros_pesquisa, headers=headers))
        print()


