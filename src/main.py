from src.api.kairos_client import KairosClient
from src.services.people_service import PeopleService
from src.services.appointment_service import AppointmentService
from src.utils.file_generator import salvar_json

from src.config.settings import API_KEY, CNPJS

def main():

    for empresa, cnpj in CNPJS.items():

        print(f"\nBuscando pessoas da empresa: {empresa}")

        client = KairosClient(
            identifier=cnpj,
            key=API_KEY
        )

        people_service = PeopleService(client)
        appointment_service = AppointmentService(client)

        people = people_service.get_all_people()

        salvar_json(people, f"people_{empresa}.json")

        print(f"Pessoas da empresa {empresa} salvas com sucesso")


    print("\nProcesso finalizado")


if __name__ == "__main__":
    main()