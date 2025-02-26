# Limpar o terminal 
import os
os.system("clear")

# Elabore um algoritimo para solicitar ao usuario o login e senha e ao final mostre na tela:
# Considere que os dados do usuario ja estao cadastrados.
# Caso o login e senha estejam corretos, mostre a mensagem:
# "Bem-vindo!"
# Caso contrario, mostre a mensagem:
# "Login ou senha invalidos."

login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo!")
else:
    print("Login ou senha invalidos!")

