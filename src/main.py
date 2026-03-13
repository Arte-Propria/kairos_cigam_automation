from src.api.kairos_client import KairosClient
from src.services.people_service import PeopleService
from src.services.appointment_service import AppointmentService
from src.utils.file_generator import salvar_arquivo_empresa
from src.config.settings import API_KEY, CNPJS
import datetime


DATA_INICIO = "09-03-2026"
DATA_FIM = "11-03-2026"
current_datetime = datetime.datetime.now()

def main():

    empresa = "ARTE_GLOBAL"
    cnpj = CNPJS[empresa]

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



from src.api.kairos_client import KairosClient
from src.services.people_service import PeopleService
from src.services.appointment_service import AppointmentService
from src.utils.file_generator import salvar_arquivo_empresa
from src.config.settings import API_KEY, CNPJS
import datetime


DATA_INICIO = "09-03-2026"
DATA_FIM = "11-03-2026"


def main():

    current_datetime = datetime.datetime.now()

    for empresa, cnpj in CNPJS.items():

        print(f"\nEmpresa: {empresa} - {current_datetime.strftime('%H:%M:%S')}")

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

            print(f"Buscando batimentos: {cpf}")

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

    print(f"\nProcesso finalizado - {datetime.datetime.now().strftime('%H:%M:%S')}")


if __name__ == "__main__":
    main()