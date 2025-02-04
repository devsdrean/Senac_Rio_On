def arearetangulo(base, altura): #Resultado
    area = base * altura
    return area

base = float(input("Valor da base? "))  #Valor de base
altura = float(input("Valor da altura? ")) #valor de altura   

AR = arearetangulo(base, altura)  #Ar = area do retangulo

print("Base:", base, "Altura:", altura, "Área é:", AR) # Resultado
