import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class funcionarios:
    # Atributos: sao variaveis que pertencem a classe.
    nome: str
    data_nascimento: str
    RG: int
    CPF: int

    # Metodo: e uma funçao que pertence a classe.
    # Este metodo para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n data_nascimento: {self.data_nascimento} \n RG: {self.RG}\n CPF: {self.CPF}")

lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS= 1

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionarios = funcionarios(
                    nome = input("Digite o nome do funcionario: "),
                    data_nascimento = float(input("Digite a data de nascimento: ")),
                    RG = int(input("Digite o numero: ")),
                    CPF = int(input("Digite o numero: "))
            )
    lista_de_funcionarios.append(funcionarios)
    print()

nome_arquivo = "catalogo_funcionarios.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for funcionarios in lista_de_funcionarios:
        arquivo_livros.write(f"{funcionarios.nome}, {funcionarios.autor}, {funcionarios.categoria}, {funcionarios.preço} \n")
