vertices = ["A", "B", "C", "D"]

arestas = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "A")
]

def matriz_adjacencia(vertices, arestas):
    indice = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)

    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for u, v in arestas:
        i = indice[u]
        j = indice[v]

        matriz[i][j] = 1
        matriz[j][i] = 1 #grafo nao direcionado

        return matriz
    
matriz = matriz_adjacencia(vertices, arestas)

print("Matriz de adjacência: ")
print ("    ", "   ".join(vertices))

for i, linha in enumerate(matriz):
    print(vertices[i], linha)