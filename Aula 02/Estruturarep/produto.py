produtos = {
    'mouse': 50.00,
    'teclado': 100.00,
    'monitor': 600.00,
    'desk': 300.00,
    'webcam': 150.00
}

produto_busca = input("Digite o nome do produto: ").lower()

if produto_busca in produtos:
    print(f"O preço de {produto_busca} é R$ {produtos[produto_busca]:.2f}")
else:
    print("Produto não encontrado.")