import heapq


def dijkstra(grafo, origem):
    """
    Calcula o menor caminho da origem para todos os vértices.

    grafo:
        Dicionário no formato:
        {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1}
        }
    """

    # Inicializa todas as distâncias como infinito
    distancias = {
        vertice: float('inf')
        for vertice in grafo
    }

    # A distância da origem para ela mesma é 0
    distancias[origem] = 0

    # Guarda o vértice anterior no menor caminho
    anteriores = {
        vertice: None
        for vertice in grafo
    }

    # Fila de prioridade
    fila = [(0, origem)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        # Ignora caminhos que já ficaram maiores
        if distancia_atual > distancias[vertice_atual]:
            continue

        # Percorre os vizinhos
        for vizinho, peso in grafo[vertice_atual].items():

            nova_distancia = distancia_atual + peso

            # Encontrou um caminho menor?
            if nova_distancia < distancias[vizinho]:

                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = vertice_atual

                heapq.heappush(
                    fila,
                    (nova_distancia, vizinho)
                )

    return distancias, anteriores


def caminho_minimo(anteriores, origem, destino):
    """
    Reconstrói o caminho mínimo entre origem e destino.
    """

    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.reverse()

    # Não existe caminho entre origem e destino
    if caminho[0] != origem:
        return None

    return caminho


#####################################################
# EXEMPLO DE GRAFO
#####################################################

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2},
}

origem = 'A'

distancias, anteriores = dijkstra(grafo, origem)

print(f"Menores caminhos partindo de {origem}:\n")

for destino in grafo:

    caminho = caminho_minimo(
        anteriores,
        origem,
        destino
    )

    print(
        f"{origem} -> {destino}: "
        f"distância = {distancias[destino]}, "
        f"caminho = {caminho}"
    )