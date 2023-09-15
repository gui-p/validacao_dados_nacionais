from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self) -> str:
        meses_do_ano = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano.get(meses_cadastro, "Chave inválida")

    def dia_semana(self) -> str:
        lst_dia_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia_da_semana = self.momento_cadastro.weekday()
        return lst_dia_da_semana[dia_da_semana]

    def formata_data(self) -> str:
        data_formatada: str = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_de_cadastro(self) -> "datetime.timedelta":
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
