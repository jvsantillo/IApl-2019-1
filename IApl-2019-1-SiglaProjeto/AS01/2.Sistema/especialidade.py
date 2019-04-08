class Especialidade:
    
    #Construtor:
    def __init__ (self, codigo, descricao, dt_ini, dt_exc):
        self.codigo = codigo
        self.descricao = descricao
        self.dt_ini = dt_ini
        self.dt_exc = dt_exc    
    
    #Métodos Get e Set:

    def get_esp_descricao(self):
        return self.descricao
    def set_esp_descricao(self,descricao):
        self.descricao = descricao

    def get_esp_codigo(self):
        return self.codigo
    def set_esp_codigo(self,esp_codigo):
        self.codigo = esp_codigo

    def get_esp_dtIni(self):
        return self.dt_ini
    def set_esp_dtIni(self, esp_dt_Ini):
        self.dt_ini = esp_dt_Ini

    def get_esp_dt_exec(self):
        return self.dt_exc  
    def set_esp_dt_exec(self, esp_dt_exc):
        self.dt_exc = esp_dt_exc
    