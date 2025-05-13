import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    pai = {vertice: None for vertice in grafo}
    distancias[origem] = 0

    fila = [(0, origem)]

    while fila:
        distancia_atual, atual = heapq.heappop(fila)

        if distancia_atual > distancias[atual]:
            continue
        for vizinho, peso in grafo[atual]: 
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                pai[vizinho] = atual
                heapq.heappush(fila, (distancia, vizinho))

    return distancias, pai

def reconstruir_caminhos(pai, origem):
    caminhos = {}

    for destino in pai:
        if destino == origem:
            caminhos[destino] = [origem]
            continue

        if pai[destino] is None:
            caminhos[destino] = None  # sem caminho
            continue

        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, atual)
            atual = pai[atual]
        caminhos[destino] = caminho

    return caminhos

# Grafo de teste
grafo_teste = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('A', 1)],
    'C': [('B', 2), ('A', 4)],
}

# Executando o algoritmo
resultado, predecessores = dijkstra(grafo_teste, 'B')
caminhos = reconstruir_caminhos(predecessores, 'B')

# Imprimindo o resultado
print("Distâncias a partir do vértice 'B':")
for vertice, distancia in resultado.items():
    print(f"{vertice}: {distancia}")

print("\nCaminhos mínimos a partir de 'B':")
for destino, caminho in caminhos.items():
    print(f"A → {destino}: {caminho}")

# Validação automática




