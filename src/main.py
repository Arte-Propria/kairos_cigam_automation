### PROJETO PREPARADO PARA AUTOMAÇÃO

from src.api.kairos_client import KairosClient
from src.services.people_service import PeopleService
from src.services.appointment_service import AppointmentService
from src.utils.file_generator import salvar_arquivo_empresa
from src.config.settings import API_KEY, CNPJS
from dateutil.relativedelta import relativedelta
import datetime
import time

current_datetime = datetime.datetime.now()

MES_ANTERIOR = current_datetime - relativedelta(months=1)
DATA_INICIO = MES_ANTERIOR.strftime("20-%m-%Y") # PEGA SEMPRE O DIA 20 DO MÊS ANTERIOR (20 = dia de fechamento) - 1 MES
DATA_FIM = current_datetime.strftime("20-%m-%Y") # PEGA SEMPRE O DIA 20 DO MÊS ATUAL (20 = dia de fechamento)



def main():

    print(f"\nProcesso iniciado - {current_datetime.strftime("%H:%M:%S")}")

    if current_datetime != current_datetime.strftime("21-%m-%Y"):   # RODARÁ APENAS NO DIA 21 (UM DIA DEPOIS DO FECHAMENTO PARA PEGAR O MES FECHADO)
        print(f"\nHoje não é dia de execução - {current_datetime.strftime("%H:%M:%S")}")

    else:
        for empresa, cnpj in CNPJS.items():
            time.sleep(0.2)

            print(f"\nEmpresa: {empresa} - {current_datetime.strftime("%H:%M:%S")}")

            client = KairosClient(
                identifier=cnpj,
                key=API_KEY
                
            )

            people_service = PeopleService(client)
            appointment_service = AppointmentService(client)

            people = people_service.get_all_people()

            todas_linhas = []

            for pessoa in people:
                id_pessoa = pessoa["Id"]
                cpf = pessoa.get("Cpf")

                if not cpf:
                    continue

                cpf = ''.join(filter(str.isdigit, cpf))

                print(f"Buscando batimentos: {cpf} - {current_datetime.strftime("%H:%M:%S")}")

                appointments = appointment_service.get_appointments(
                    id_pessoa,
                    DATA_INICIO,
                    DATA_FIM
                )

                linhas = appointment_service.gerar_linhas(
                    appointments,
                    cpf
                )

                todas_linhas.extend(linhas)

            salvar_arquivo_empresa(
                empresa,
                cnpj,
                todas_linhas,
                DATA_INICIO,
                DATA_FIM
            )

    print(f"\nProcesso finalizado - {current_datetime.strftime("%H:%M:%S")}")


if __name__ == "__main__":
    main()

