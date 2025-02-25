def user_info(name, age, **kwargs):
    print(f"Nome: {name}")
    print(f"Idade: {age}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

user_info("André", 30, cidade="Rio de Janeiro", profissao="analista de suporte", hobby="videogame")
