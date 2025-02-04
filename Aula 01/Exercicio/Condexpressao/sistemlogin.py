usuario = input("nome de usuario: ")
senha = input("senha:")

if usuario == "admin" and senha == "root":
    print("acesso garantido")
else:
    print("acesso negado")