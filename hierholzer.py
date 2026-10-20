from collections import defaultdict

def criar_grafo(arestas):
    grafo = defaultdict(list)

    for u, v in arestas:
        grafo[u].append(v)
        grafo[v].append(u)

    return grafo


def todos_graus_pares(grafo):
    for vertice in grafo:
        if len(grafo[vertice]) %2 != 0:
            return False

    return True

def hierholzer(grafo, inicio):
    # Faz uma copia do grafo para nao alterar o original

    grafo_temp = {v: vizinhos[:] for v, vizinhos in grafo.items()
    }

    pilha = [inicio]
    circuito = []

    while pilha:
        vertice_atual = pilha[-1]

        if grafo_temp[vertice_atual]:
            proximo = grafo_temp[vertice_atual].pop()

            # Remove a aresta nos dois sentidos

            grafo_temp[proximo].remove(vertice_atual)

            pilha.append(proximo)
        else:
            circuito.append(pilha.pop())

    circuito.reverse()

    return circuito

arestas = [

    ("A", "B"),
    ("B", "C"),
    ("C", "A"),
    ("A", "D"),
    ("D", "E"),
    ("E", "A"),

]

grafo = criar_grafo(arestas)

if todos_graus_pares(grafo):
    circuito = hierholzer(grafo, "A")
    print("Circuito Euleriano: ")
    print(circuito)
else:
    print("O grafo não possui circuito Euleriano.")
