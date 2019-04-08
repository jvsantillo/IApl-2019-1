from prestador import Prestador
from especialidade import Especialidade
from prestador_especialidade import Prestador_Especialidade



prestador1 = Prestador(1, "João", "08/04/2019", "01/05/2019", 2)

print(prestador1.get_cod())
print(prestador1.get_dtIni())

prestador1.set_cod(2)

print(prestador1.get_cod())
print(prestador1.get_pre_codigo())

especialidade1 = Especialidade(1, "Pediatria", "01/04/2019", "08/04/2019")

print(especialidade1.get_esp_codigo())
print(especialidade1.get_esp_descricao())

prestador_especialidade1 = Prestador_Especialidade(prestador1, especialidade1, "20/04/2019", "20/04/2020")
print(prestador_especialidade1.get_pre_codigo())
print(prestador_especialidade1.get_esp_codigo())

