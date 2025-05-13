#construção de um grafo

grafo = {
    0: {
        "info": [2, False, False, 0],  # [agua_necessaria, posto, lago, estado_fogo]
        "vizinhos": [(1, 3), (2, 5)]   # (vizinho, custo)
    },
    1: {
        "info": [1, True, False, 0],
        "vizinhos": [(0, 3), (3, 2)]
    },
    2: {
        "info": [3, False, True, 0],
        "vizinhos": [(0, 5), (3, 4)]
    },
    3: {
        "info": [2, False, False, 0],
        "vizinhos": [(1, 2), (2, 4), (4, 6)]
    },
    4: {
        "info": [2, False, False, 0],
        "vizinhos": [(3, 6), (5, 1)]
    },
    5: {
        "info": [3, False, False, 0],
        "vizinhos": [(4, 1), (6, 3)]
    },
    6: {
        "info": [1, False, True, 0],
        "vizinhos": [(5, 3), (7, 2)]
    },
    7: {
        "info": [2, False, False, 0],
        "vizinhos": [(6, 2), (8, 4)]
    },
    8: {
        "info": [1, True, False, 0],
        "vizinhos": [(7, 4), (9, 5)]
    },
    9: {
        "info": [2, False, False, 0],
        "vizinhos": [(8, 5)]
    }
}


# grafo = {
#     'A': [[3, False, False, 0], [('B', 1), ('C', 2), ('G', 5), ('F', 3)]],
#     'B': [[2, False, False, 0], [('B', 1), ('C', 4), ('H', 4)]],
#     'C': [[1, False, False, 0], [('A', 3), ('E', 4)]], 
#     'D': [[4, False, False, 0], [('B', 2), ('I', 1), ('D', 3)]],
#     'E': [[5, False, False, 0], [('H', 2), ('G', 4), ('I', 1)]],
#     'F': [[6, False, False, 0], [('C', 3), ('D', 2), ('H', 1)]],
#     'G': [[6, False, False, 0], [('A', 5), ('I', 5),('B', 2), ('C', 4), ('D', 1)]],
#     'H': [[5, False, False, 0], [('E', 4), ('G', 2), ('E', 1), ('D', 3)]],
#     'I': [[4, False, False, 0], [('E', 1), ('G', 5), ('H', 2), ('F', 3)]],
# }

print(grafo)