class Pessoa:
    
    #Construtor:
    def __init__ (self, codigo, nome, dt_ini, dt_exec):
        self.codigo = codigo
        self.nome = nome
        self.dt_ini = dt_ini
        self.dt_exec = dt_exec    
    
    #Métodos Get e Set:

    def get_name(self):
        return self.nome
    def set_name(self,name):
        self.nome = name

    def get_cod(self):
        return self.codigo
    def set_cod(self,cod):
        self.codigo = cod

    def get_dtIni(self):
        return self.dt_ini
    def set_dtIni(self, dtIni):
        self.dt_ini = dtIni

    def get_dt_exec(self):
        return self.dt_exec  
    def set_dt_exec(self, dt_exec):
        self.dt_exec = dt_exec
    