from acesso_cep import BuscaEndereco
import requests

cep_num = "06515055"
cep = BuscaEndereco("06515055")

bairro, cidade, uf = cep.acessa_via_cep()

print(bairro, cidade, uf)



