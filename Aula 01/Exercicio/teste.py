# Solicita ao usuário que insira uma nota de 0 a 100
nota = int(input('Digite uma nota de 0 a 100: '))
 
# Atribui um conceito à nota
if nota >= 90:
    conceito = 'A'
elif nota >= 80:
    conceito = 'B'
elif nota >= 70:
    conceito = 'C'
elif nota >= 60:
    conceito = 'D'
elif nota >= 50:
    conceito = 'E'
else:
    conceito = 'F'    
 
# Exibe o conceito atribuído
print(f'O conceito atribuído à nota {nota} é {conceito}')