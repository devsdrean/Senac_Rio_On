def celsiusparafaren (c): #Define o calculo da conversão
    return (c * 9/5) + 32

celsius = float(input("Qual a temperatura em celsius? ")) #Solicita o valor
fahrenheit = celsiusparafaren(celsius) #especifica o valor de fahrenheit em celsius
print(f"{celsius:.0f}Cº é igual a {fahrenheit:.1f}Fº") #resultado final