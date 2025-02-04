def verparouimpar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

num = int(input("Digite um numero: "))  
resultado = verparouimpar(num)

print(f"O numero {num} é {resultado}.")
