import heapq

# ==========================================
# KRUSKAL
# ==========================================

class UnionFind:
    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}

    def encontrar(self, v):
        if self.pai[v] != v:
            self.pai[v] = self.encontrar(self.pai[v])
        return self.pai[v]

    def unir(self, a, b):
        raiz_a = self.encontrar(a)
        raiz_b = self.encontrar(b)

        if raiz_a != raiz_b:
            self.pai[raiz_b] = raiz_a
            return True

        return False


def kruskal_passo_a_passo(vertices, arestas):
    print("\n" + "=" * 60)
    print("ALGORITMO DE KRUSKAL")
    print("=" * 60)

    arestas_ordenadas = sorted(arestas, key=lambda x: x[2])

    print("\nArestas ordenadas pelo peso:")

    for origem, destino, peso in arestas_ordenadas:
        print(f"{origem} -- {destino} : {peso}")

    uf = UnionFind(vertices)

    arvore = []
    custo_total = 0

    passo = 1

    for origem, destino, peso in arestas_ordenadas:

        print("\n" + "-" * 50)
        print(f"PASSO {passo}")

        print(
            f"Analisando Aresta: "
            f"{origem} -- {destino} "
            f"(peso = {peso})"
        )

        if uf.unir(origem, destino):

            print("Resultado: ACEITA")

            arvore.append((origem, destino, peso))

            custo_total += peso

        else:

            print("Resultado: REJEITADA")
            print("Motivo: formaria um ciclo.")

        print("\nÁrvore Atual:")

        if arvore:
            for a, b, p in arvore:
                print(f"{a} -- {b} : {p}")
        else:
            print("Nenhuma aresta ainda.")

        print(f"Custo acumulado = {custo_total}")

        passo += 1

        if len(arvore) == len(vertices) - 1:
            break

    print("\n" + "=" * 60)
    print("RESULTADO FINAL - KRUSKAL")
    print("=" * 60)

    for origem, destino, peso in arvore:
        print(f"{origem} -- {destino} : {peso}")

    print(f"\nCusto Total da AGM = {custo_total}")

    return arvore, custo_total


# ==========================================
# PRIM
# ==========================================

def prim_passo_a_passo(grafo, inicio):

    print("\n" + "=" * 60)
    print("ALGORITMO DE PRIM")
    print("=" * 60)

    visitados = set()
    arvore = []
    custo_total = 0

    fila = [(0, None, inicio)]

    passo = 1

    while fila:

        peso, origem, atual = heapq.heappop(fila)

        if atual in visitados:
            continue

        print("\n" + "-" * 50)
        print(f"PASSO {passo}")

        if origem is None:

            print(f"Vértice inicial escolhido: {atual}")

        else:

            print("Menor aresta disponível:")
            print(
                f"{origem} -- {atual} "
                f"(peso = {peso})"
            )

        visitados.add(atual)

        if origem is not None:

            arvore.append(
                (origem, atual, peso)
            )

            custo_total += peso

            print("Resultado: ARESTA ADICIONADA")

        print(
            f"\nVértices visitados: "
            f"{sorted(visitados)}"
        )

        print("\nÁrvore atual:")

        if arvore:

            for a, b, p in arvore:
                print(f"{a} -- {b} : {p}")

        else:
            print("Nenhuma aresta ainda.")

        print(f"Custo acumulado = {custo_total}")

        print("\nNovas arestas candidatas:")

        for vizinho, peso_aresta in grafo[atual]:

            if vizinho not in visitados:

                heapq.heappush(
                    fila,
                    (
                        peso_aresta,
                        atual,
                        vizinho
                    )
                )

                print(
                    f"{atual} -- {vizinho} "
                    f"(peso = {peso_aresta})"
                )

        passo += 1

    print("\n" + "=" * 60)
    print("RESULTADO FINAL - PRIM")
    print("=" * 60)

    for origem, destino, peso in arvore:
        print(f"{origem} -- {destino} : {peso}")

    print(f"\nCusto total da AGM = {custo_total}")

    return arvore, custo_total


# ==========================================
# GRAFO DE EXEMPLO
# ==========================================

vertices = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

arestas = [
    ("A", "B", 2),
    ("A", "C", 4),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 3),
    ("C", "E", 6),
    ("D", "E", 2)
]


grafo = {

    "A": [
        ("B", 2),
        ("C", 4)
    ],

    "B": [
        ("A", 2),
        ("C", 1),
        ("D", 5)
    ],

    "C": [
        ("A", 4),
        ("B", 1),
        ("D", 3),
        ("E", 6)
    ],

    "D": [
        ("B", 5),
        ("C", 3),
        ("E", 2)
    ],

    "E": [
        ("C", 6),
        ("D", 2)
    ]
}


# ==========================================
# EXECUÇÃO
# ==========================================

kruskal_passo_a_passo(
    vertices,
    arestas
)

prim_passo_a_passo(
    grafo,
    "B"
)



# Árvore Geradora Mínima

# É um subconjunto das arestas de um grafo conexo, nao direcionado e ponderado que:
#   - conecta todos os vertices
#   - nao possui ciclos
#   - possui exatamente n-1 arestas
#   - tem a menor soma possivel de pesos
