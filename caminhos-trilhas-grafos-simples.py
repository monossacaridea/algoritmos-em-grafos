def encontrar_caminhos(grafo, origem, destino):
    
    caminhos = []

    def dfs(atual, caminho):

        if atual == destino:
            caminhos.append(caminho.copy())
            return

        for vizinho in grafo[atual]:

            if vizinho not in caminho:

                caminho.append(vizinho)

                dfs(
                    vizinho,
                    caminho
                )

                caminho.pop()

    dfs(origem, [origem])

    return caminhos


def encontrar_trilhas(grafo, origem, destino):

    trilhas = []

    def dfs(atual, trilha, arestas_usadas):

        if atual == destino:
            trilhas.append(trilha.copy())
            return

        for vizinho in grafo[atual]:

            aresta = tuple(sorted((atual, vizinho)))

            if aresta not in arestas_usadas:

                arestas_usadas.add(aresta)

                trilha.append(vizinho)

                dfs(
                    vizinho,
                    trilha,
                    arestas_usadas
                )

                trilha.pop()

                arestas_usadas.remove(aresta)

    dfs(
        origem,
        [origem],
        set()
    )

    return trilhas


# ================================================================
# EXEMPLO DE GRAFO
# ================================================================

grafo = {

    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']

}

origem = 'A'
destino = 'D'


# ================================================================
# CAMINHOS
# ================================================================

caminhos = encontrar_caminhos(
    grafo,
    origem,
    destino
)

print("\nCAMINHOS:")
print("-" * 40)

for i, caminho in enumerate(caminhos, start=1):

    print(
        f"Caminho {i}: "
        + " -> ".join(caminho)
    )


# ================================================================
# TRILHAS
# ================================================================

trilhas = encontrar_trilhas(
    grafo,
    origem,
    destino
)

print("\nTRILHAS:")
print("-" * 40)

for i, trilha in enumerate(trilhas, start=1):

    print(
        f"Trilha {i}: "
        + " -> ".join(trilha)
    )