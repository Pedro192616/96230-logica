import os 
os.system("clear")

login_cadastrado = "Pedro" 
senha_cadastrada = "1234"


login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while True:
    if login == login_cadastrado and senha == senha_cadastrada:
        print("Acesso permitido.")
        break
    
    else: 
        print("Acesso negado.\n")
        
