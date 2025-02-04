def classificarnota(nota):
    if nota >= 90:
        return "Nota A"
    elif nota >= 80:
        return "Nota B"
    elif nota >= 70:
        return "Nota C"
    elif nota >= 60:
        return "Nota D"
    elif nota >= 50:
        return "Nota E"
    else:
        return "Nota F"

nota = float(input("Digite a nota (0 a 100): "))

classificacao = classificarnota(nota)
print(f"{classificacao}")

