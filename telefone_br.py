import re

class TelefoneBr:

    def __init__(self, telefone: str):
        if(self.__valida_telefone(telefone)):
            self.numero = telefone
        else:
            raise ValueError("Número Incorreto")

    def __valida_telefone(self, telefone: str) -> bool:
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        verificador = re.search(padrao, telefone)
        if(verificador):
            return True
        else:
            return False

    def cria_mascara(self) -> str:
        padrao = "([0-9]{2})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        partes_numero = re.search(padrao, self.numero)
        mascara_numero = "+{}({}){}-{}".format(
            partes_numero.group(1),
            partes_numero.group(2),
            partes_numero.group(3),
            partes_numero.group(4),
        )
        return mascara_numero

    def __str__(self):
        return self.cria_mascara()
