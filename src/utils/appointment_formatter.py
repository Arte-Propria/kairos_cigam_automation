from datetime import datetime


def formatar_batimento(ap):

    # IdApont com 9 posições
    id_apont = str(ap["IdApont"]).zfill(9)

    # Data base
    data = datetime(
        ap["AnoColeta"],
        ap["MesColeta"],
        ap["DiaColeta"],
        ap["HoraColeta"],
        ap["MinutoColeta"],
        ap["SegundoColeta"]
    )

    # Data sem segundos
    data_sem_seg = data.strftime("%Y-%m-%dT%H:%M:00")

    # Data com segundos
    data_com_seg = data.strftime("%Y-%m-%dT%H:%M:%S")

    cpf = ap["PIS"]

    linha = (
        f"{id_apont}7"
        f"{data_sem_seg}"
        f"-0300"
        f"{cpf} "
        f"{data_com_seg}"
        f"-03000200"
    )

    return linha