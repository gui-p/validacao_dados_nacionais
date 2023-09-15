import requests


class BuscaEndereco:

    def __init__(self, cep: str):
        cep = str(cep)
        if (self._valida_cep(cep)):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.cep_formatado()

    def _valida_cep(self, cep: str) -> bool:
        return True if len(cep) == 8 else False

    def cep_formatado(self) -> str:
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self) -> tuple:
        url: str = f"https://viacep.com.br/ws/{self.cep}/json"
        resposta_web: "requests.models.Response" = requests.get(url)
        dados: dict = resposta_web.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
