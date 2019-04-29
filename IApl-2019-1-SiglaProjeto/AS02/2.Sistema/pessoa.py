class Pessoa:
    
    #Construtor:
    def __init__ (self, PessoaID, Nome, DataInclusao, DataExclusao):
        self.PessoaID = PessoaID
        self.Nome = Nome
        self.DataInclusao = DataInclusao
        self.DataExclusao = DataExclusao    
    
    #Métodos Get e Set:

    def get_Nome(self):
        return self.Nome
    def set_Nome(self,Nome):
        self.Nome = Nome

    def get_PessoaID(self):
        return self.PessoaID
    def set_PessoaID(self,PessoaID):
        self.PessoaID = PessoaID

    def get_DataInclusao(self):
        return self.DataInclusao
    def set_DataInclusao(self, DataInclusao):
        self.DataInclusao = DataInclusao

    def get_DataExclusao(self):
        return self.DataExclusao  
    def set_DataExclusao(self, DataExclusao):
        self.DataExclusao = DataExclusao
