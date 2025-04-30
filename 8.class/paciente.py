import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Paciente:
    # Atributos: sao variaveis que pertencem a classe.
    nome: str
    idade: int

    # Metodo: e uma funçao que pertence a classe.
    # Este metodo para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n")


# Criando uma lista.
lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

# Atribuindo dados dos pacientes.
for i in range (QUANTIDADE_PACIENTES):
    paciente = Paciente(
                    nome = input("Digite seu nome: "),
                    idade = int(input("Digite sua idade: "))
            )
    lista_de_pacientes.append(paciente)

# Exibindo dados do paciente.
print("\nExibindo dados do usuario.")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()
