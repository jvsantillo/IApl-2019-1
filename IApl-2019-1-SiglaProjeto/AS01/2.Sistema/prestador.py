from pessoa import Pessoa

class Prestador(Pessoa):
    
    #Construtor com herança da classe pessoa:
    def __init__ (self, pre_codigo, nome, dt_inc, dt_exec, codigo):
        self.pre_codigo = pre_codigo
        super().__init__(codigo, nome, dt_inc, dt_exec)
           
    
    #Métodos Get e Set:

    def get_pre_codigo(self):
        return self.pre_codigo
    def set_pre_codigo(self,pre_codigo):
        self.pre_codigo = pre_codigo