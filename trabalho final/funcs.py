import random 

def criarfogo(grafo, lago, posto):
    while True:
        try:
            # Gera um índice aleatório para o grafo
            fagulha = random.randint(0, len(grafo) - 1)
            # Verifica se o índice é um lago ou um posto
            if fagulha in lago or fagulha in posto:
                continue
            else:
                # Marca o vértice como "pegando fogo"
                vertice = chr(65 + fagulha) 
                grafo[vertice][0][3] = 1  # Ajuste conforme a estrutura do grafo
                print(f"Fogo iniciado em {vertice}.")
                break  
        except IndexError:
            print("Não há vértices válidos para pegar fogo (todos são lagos ou postos).")
            break

def em_chamas(grafo):
    # Verifica se algum vértice está pegando fogo
    for vertice in grafo:
        if grafo[vertice][0][3] == 1:  # Ajuste conforme a estrutura do grafo
            return True
    return False