class Prestador:
    
    #Construtor:
    def __init__ (self, name, cod, dtIni, dtFim):
        self.name = name
        self.cod = cod
        self.dtIni = dtIni
        self.dtFim = dtFim    
    
    #Métodos Get e Set:

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name

    def get_cod(self):
        return self.cod
    def set_cod(self,cod):
        self.cod = cod

    def get_dtIni(self):
        return self.dtIni
    def set_dtIni(self, dtIni):
        self.dtIni = dtIni

    def get_dtFim(self):
        return self.dtFim  
    def set_dtFim(self, dtFim):
        self.dtFim = dtFim
    