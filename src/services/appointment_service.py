from src.utils.appointment_formatter import formatar_batimento


class AppointmentService:

    def __init__(self, client):
        self.client = client

    def get_appointments(self, id_pessoa, data_inicio, data_fim):

        payload = {
            "IdsPessoa": [id_pessoa],
            "MarcacaoColetadaAPI": False,
            "DataInicio": data_inicio,
            "DataFim": data_fim,
            "ResponseType": "AS400V1"
        }

        response = self.client.post(
            "Appointment/GetAppointmentsPointer",
            payload
        )

        return response["Obj"]

    def gerar_linhas(self, appointments):

        linhas = []

        for ap in appointments:
            linha = formatar_batimento(ap)
            linhas.append(linha)

        return linhas