class Especialidade:
    
    #Construtor:
    def __init__ (self, EspecialidadeID, Descricao, DataInclusao, DataExclusao):
        self.EspecialidadeID = EspecialidadeID
        self.Descricao = Descricao
        self.DataInclusao = DataInclusao
        self.DataExclusao = DataExclusao    
    
    #Métodos Get e Set:

    def get_esp_Descricao(self):
        return self.Descricao
    def set_esp_Descricao(self,Descricao):
        self.Descricao = Descricao

    def get_esp_EspecialidadeID(self):
        return self.EspecialidadeID
    def set_esp_EspecialidadeID(self,esp_EspecialidadeID):
        self.EspecialidadeID = esp_EspecialidadeID

    def get_esp_DataInclusao(self):
        return self.DataInclusao
    def set_esp_DataInclusao(self, esp_DataInclusao):
        self.DataInclusao = esp_DataInclusao

    def get_esp_DataExclusao(self):
        return self.DataExclusao  
    def set_esp_DataExclusao(self, esp_DataExclusao):
        self.DataExclusao = esp_DataExclusao
