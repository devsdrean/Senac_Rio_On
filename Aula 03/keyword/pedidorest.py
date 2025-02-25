def order_food(**kwargs):
    for prato, quantidade in kwargs.items():
        print(f"{prato}: {quantidade} unidade(s)")

order_food(pizza=2, hamburguer=3, suco=1)
