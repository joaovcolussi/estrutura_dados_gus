#Linha 0
matriz = [[1,2,3], [4,5,6]]
#Coluna   0 1 2     0 1 2

#3x2
#[[0,0], [0,0] [0,0]]

# [[], [], []]
# transposta = []

# for coluna in range(len(matriz[0])):
#   linha_transposta = []
  
#   for linha in range(len(matriz)):
#     linha_transposta.append(linha_transposta)

transposta = [
  [
    matriz[linha][coluna]
    for linha in range(len(matriz))
  ]
  for coluna in range(len(matriz[0]))
]
print(transposta)