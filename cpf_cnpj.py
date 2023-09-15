from validate_docbr import CPF, CNPJ
from abc import ABC, abstractmethod

class Documento:

    @staticmethod
    def cria_documento(documento: int):
        documento: str = str(documento)
        if(len(documento) == 11):
            return DocCpf(documento)
        elif(len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!!")

class DocCpf:

    def __init__(self, documento: str):
        if(self.valida(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def valida(self, documento: str) -> bool:
        validador = CPF()
        validade: bool = validador.validate(documento)
        return validade

    def formata(self, documento: str) -> str:
        mascara = CPF()
        mascara = mascara.mask(documento)
        return mascara

    def __str__(self):
        return self.formata(self.cpf)

class DocCnpj:

    def __init__(self, documento: str):
        if(self.valida(documento)):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida(self, documento: str) -> bool:
        validador = CNPJ()
        validade: bool = validador.validate(documento)
        return validade

    def formata(self, documento: str) -> str:
        mascara = CNPJ()
        mascara = mascara.mask(documento)
        return mascara

    def __str__(self):
        return self.formata(self.cnpj)

