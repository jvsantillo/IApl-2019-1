from prestador import Prestador

prestador1 = Prestador("João", 1, "25/02/2018", "21/02/2019")

print(prestador1.get_cod())
print(prestador1.get_dtIni())

prestador1.set_cod(2)

print(prestador1.get_cod())
