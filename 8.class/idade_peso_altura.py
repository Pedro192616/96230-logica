import os
os.system("clear")


class pessoa():
    nome : str
    idade : int
    peso : float
    altura : float


print("Solicitando dados: ")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


pessoa1 = pessoa(idade, nome, peso, altura)

print("\nExibindo dados: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, peso: {pessoa1.peso}, altura: {pessoa1.altura}")