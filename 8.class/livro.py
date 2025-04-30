import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class livros:
    # Atributos: sao variaveis que pertencem a classe.
    nome: str
    autor: str
    categoria: str
    preço: float

    # Metodo: e uma funçao que pertence a classe.
    # Este metodo para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n autor: {self.autor} \n categoria: {self.categoria}\n preço: {self.preço}")

lista_de_livros = []
QUANTIDADE_LIVROS = 4

for i in range (QUANTIDADE_LIVROS):
    livros = livros(
                    nome = input("Digite o nome do livro: "),
                    autor = input("Digite o autor do livro: "),
                    categoria = input("Digite a categoria do livro: "),
                    preço = float(input("Digite o preço: "))
            )
    lista_de_livros.append(livros)
    print()

nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for livros in lista_de_livros:
        arquivo_livros.write(f"{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preço} \n")
