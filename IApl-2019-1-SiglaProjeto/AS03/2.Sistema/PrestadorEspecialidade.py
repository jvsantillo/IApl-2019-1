from prestador import Prestador
from especialidade import Especialidade

class PrestadorEspecialidade:

 #Construtor:
    def __init__ (self, ID, prestadorEspecialidadeId, DataInclusao, DataExclusao):
        self.PrestadorID = prestador.get_PrestadorID()
        self.EspecialidadeID = especialidade.get_EspecialidadeID()
        self.DataInclusao = DataInclusao
        self.DataExclusao = DataExclusao

 #Métodos Get e Set:

    def get_PrestadorID(self):
        return self.PrestadorID
    def set_PrestadorID(self,PrestadorID):
        self.PrestadorID = PrestadorID

    def get_EspecialidadeID(self):
        return self.EspecialidadeID
    def set_EspecialidadeID(self,EspecialidadeID):
        self.EspecialidadeID = EspecialidadeID

    def get_dtIni(self):
        return self.DataInclusao
    def set_dtIni(self, DataInclusao):
        self.DataInclusao = DataInclusao

    def get_DataExclusao(self):
        return self.DataExclusao  
    def set_DataExclusao(self, DataExclusao):
        self.DataExclusao = DataExclusao   


