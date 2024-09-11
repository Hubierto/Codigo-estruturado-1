import os
from models.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo

os.system("cls || clear")
funcionario1 = Funcionario(204073, "André", 20, 2.900, Setor.VENDAS, Sexo.MASCULINO) 
print(funcionario1)