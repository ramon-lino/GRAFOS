from grafo import Grafo

g = Grafo()

def ent_vertices():
    try:
        vert = input("Digite os vertives >> ")
        vert = vert.split(", ")

        for i in vert:
            g.adicionaVertice(i)
        return vert

    except:
        print("Vertices invalidos! Formato não aceito.")
        print("Digite no formato: 'A, B, C, D'")


def ent_arestas():
    dic_aux = {}
    print("As arestas devem ser informada no modelo: a1(J-C), a2(C-E), a3(C-E)")
    ares = input("Digite as arestas >> ")
    ares = ares.split(", ")

    try:
        for i in range(len(ares)):
            ares[i] = ares[i].replace(")","(")
            ares[i] = ares[i].split("(")
            g.adicionaAresta(ares[i][0], ares[i][1])
            dic_aux[ares[i][0]] = ares[i][1]

        return dic_aux
    except:
        print("Arestas invalidas! Formato não aceito ou não correspondentes aos vertices.")
        print("Digite no formato: 'a1(A-B), a2(C-D), a3(E-F)' - com conexões correspondentes aos vertices.")

def naoAdjacente(dicV = [], dicA = {}):
    lista_aux = []
    matriz_conex = []

    for i in range (len(dicV)):
        for e in dicA.keys():
            string_aux = dicA[e]

            if (dicV[i] == string_aux[0]) or (dicV == string_aux[2]):
                if dicV[i] == string_aux[0]:
                    lista_aux.append(string_aux[2])
                if dicV[i] == string_aux[2]:
                    lista_aux.append(string_aux[0])
        matriz_conex.append(lista_aux)
        lista_aux = []

    return matriz_conex

vert = ent_vertices()
ares = ent_arestas()
x = naoAdjacente(vert,ares)
print(g)
print(x)