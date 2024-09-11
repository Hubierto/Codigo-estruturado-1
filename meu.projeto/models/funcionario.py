from models.enums.setor import Setor
from models.enums.sexo import Sexo

class Funcionario:

    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo ) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"    
            f"\nNome: {self.nome}"    
            f"\nIdade: {self.idade}"    
            f"\nSalário: {self.salario}"    
            f"\nSetor:{self.setor.value}"    
            f"\nSexo: {self.setor.value}") 

 