import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class livros:
    # Atributos: sao variaveis que pertencem a classe.
    nome: str
    autor: str
    titulo: str
    biografia: str
    ano: int

    # Metodo: e uma funçao que pertence a classe.
    # Este metodo para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n autor: {self.autor} \n titulo: {self.titulo} \n biografia: {self.biografia}\n ano: {self.ano}")

lista_de_livros = []
QUANTIDADE_LIVROS = 10

for i in range (QUANTIDADE_LIVROS):
    livros = livros(
                    nome = input("Digite o nome do livro: "),
                    autor = input("Digite o autor do livro: "),
                    titulo = input("Digite o titulo do livro: "),
                    biografia = input("Digite a biografia do livro: "),
                    ano = float(input("Digite o ano de publicaçao do livro: "))
            )
    lista_de_livros.append(livros)
    print()

nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    for livros in lista_de_livros:
        arquivo_livros.write(f"{livros.nome}, {livros.autor}, {livros.titulo}, {livros.biografia}, {livros.ano} \n")
        livros.exibir_dados()

if __name__ == "__main__":
    "main"()