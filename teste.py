class UM:
    def __init__(self):
        self.nome = "marcos"
        self.cidade= 'sao paulo'

class DOIS(UM):
    def __init__(self):
        super().__init__()
        self.nome = "planta"
        self.idade = 23
    
    def getCidade(self):
        return self.cidade
    
x = DOIS()

print(x.getCidade)