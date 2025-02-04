chovendo = input("esta chovendo? sim ou nao ")
raios = input("tem raios? sim ou nao ")

if chovendo == "sim" and raios =="sim":
    print("fique em casa")
elif chovendo == "sim" or raios == "sim":
    print("cuidado ao sair")
else:
    print("pode sair seguro")