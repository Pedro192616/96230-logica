import os
os.system("clear")

class Pessoa:
    nome: str
    idade: int

class Pet:
    nome: str
    idade: int
    raça: str


pessoa1 = Pessoa("Marta", 30)
pessoa2 = Pessoa("Jose", 40)

pet1 = Pet("Toto", 4, "Pastor-alemao")
pet2 = Pet("Hulk", 6, "Pitbull")


print("Dados da pessoa: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}")


print("Dados da pessoa: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, raça: {pet1.raça}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}, raça: {pet2.raça}")
