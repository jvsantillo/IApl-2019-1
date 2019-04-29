from pessoa import Pessoa

class Prestador(Pessoa):
    
    #Construtor com herança da classe pessoa:
    def __init__ (self, PrestadorID, Nome, DataInclusao, DataExclusao, PessoaID):
        self.PrestadorID = PrestadorID
        super().__init__(PessoaID, Nome, DataInclusao, DataExclusao)
           
    
    #Métodos Get e Set:

    def get_PrestadorID(self):
        return self.PrestadorID
    def set_PrestadorID(self,PrestadorID):
        self.PrestadorID = PrestadorID
