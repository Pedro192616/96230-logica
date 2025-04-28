import os
os.system("clear")


class pessoa():
    nome : str
    email : str
    telefone : float
    endereço : float


print("Solicitando dados: ")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = float(input("Digite seu telefone: "))
endereço = float(input("Digite sua endereço: "))


pessoa1 = pessoa(nome, email, telefone, endereço)

print("\nExibindo dados: ")
print(f"Nome: {pessoa1.nome}, email: {pessoa1.email}, telefone: {pessoa1.telefone}, endereço: {pessoa1.endereço}")