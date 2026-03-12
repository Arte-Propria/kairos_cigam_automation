from pathlib import Path
from datetime import datetime


def gerar_header(empresa, cnpj, dt_inicio, dt_fim):

    data_geracao = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-0300")

    header = (
         "000000000"
        + f"{cnpj}"
        + "000000000000000"
        + f"{empresa}".ljust(120)
        + f"{dt_inicio}"
        + f"{dt_fim}"
        + f"{data_geracao}"
    )

    return header

def gerar_trailer(qtd_linhas):

    return f"999999999{str(qtd_linhas).zfill(60)}"

def salvar_arquivo_empresa(empresa, cnpj, linhas, dt_inicio, dt_fim):

    pasta = Path("data/raw")
    pasta.mkdir(parents=True, exist_ok=True)

    caminho = pasta / f"batimentos_{empresa}_{dt_inicio}_{dt_fim}.txt"

    header = gerar_header(empresa, cnpj, dt_inicio, dt_fim)
    trailer = gerar_trailer(len(linhas))

    with open(caminho, "w", encoding="utf-8") as f:

        f.write(header + "\n")

        for linha in linhas:
            f.write(linha + "\n")

        f.write(trailer + "\n")
