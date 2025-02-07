# Matriz original
matrizOriginal = [[1,2,3], [4,5,6]]

for i in matrizOriginal:
  print(i)

# Inicializando uma lista vazia para armazenar a matriz transposta
matrizT = []

# Número de linhas e colunas da matriz original
numLinhas = len(matrizOriginal)
numColunas =len(matrizOriginal[0])

# Percorrendo cada coluna da matriz original
for i in range(numColunas):
  # Inicializando uma nova linha para a matriz transposta  
  novaLinha =[]

  # Percorrendo cada linha da matriz original  
  for j in range(numLinhas):
  # Adicionando o elemento A[j][i] à nova linha
    novaLinha.append(matrizOriginal[j][i])


# Adicionando a nova linha à matriz transposta
matrizT.append(novaLinha)


#Exibindo Matriz Transposta
for linha in matrizT:
  print(linha)
