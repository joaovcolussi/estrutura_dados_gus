#exercicio 1

numeros = [1,3,5,3,7,9,1,5,9,11]
unicos =[]

for i in numeros:
  if numeros not in unicos:
    unicos.append(i)

print(unicos)
  

#exercicio 2

Gabarito = ["A", "B", "B", "C", "E", "D", "D", "E", "C", "B"]

Lara = ["B","B", "A", "E", "E", "C", "D", "A", "C", "D"]
Marcos = ["D","B", "B", "C", "A", "E", "B", "A", "C", "A"]
contador_nota = 0

for i in range(len(Gabarito)):
  if Lara[i] == Gabarito[i]:
    contador_nota +=1
    

print(f"A nota de Lara é {contador_nota}")
