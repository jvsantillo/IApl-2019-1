from prestador import Prestador
from especialidade import Especialidade

class Prestador_Especialidade:

 #Construtor:
    def __init__ (self, prestador, especialidade, dt_ini, dt_exc):
        self.pre_codigo = prestador.get_pre_codigo()
        self.esp_codigo = especialidade.get_esp_codigo()
        self.dt_ini = dt_ini
        self.dt_exc = dt_exc

 #Métodos Get e Set:

    def get_pre_codigo(self):
        return self.pre_codigo
    def set_pre_codigo(self,pre_codigo):
        self.pre_codigo = pre_codigo

    def get_esp_codigo(self):
        return self.esp_codigo
    def set_esp_codigo(self,esp_codigo):
        self.esp_codigo = esp_codigo

    def get_dtIni(self):
        return self.dt_ini
    def set_dtIni(self, dt_Ini):
        self.dt_ini = dt_Ini

    def get_dt_exc(self):
        return self.dt_exc  
    def set_dt_exc(self, dt_exc):
        self.dt_exc = dt_exc  


