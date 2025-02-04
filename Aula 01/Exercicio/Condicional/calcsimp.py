def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    
num1 = float(input("digite o primeiro numero "))
num2 = float(input("digite o primeiro numero "))
operacao = input("escolha a operação (+, -, *, /)")

resultado = calcular(num1, num2, operacao)
print(f"o resultado de {num1} {operacao} {num2} e: {resultado}")