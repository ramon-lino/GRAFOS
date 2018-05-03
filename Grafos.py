from grafo import Grafo

## Função para entrada dos vertices ##
def ent_vertices():
    try:
        vert = input("Digite os Vertices do Grafo >>>  ")
        vert = vert.split(", ")     # Separando a String de entrada em uma lista com cada Vertices como elemento.

        for i in vert:
            g.adicionaVertice(i)    # Adicionando Vertices na variavel " g ".
        return vert

    except:
        print("Vertices invalidos! Formato não aceito.")
        print("Digite no formato: 'A, B, C, D'")

def ent_arestas():
    dic_aux = {}
    #print("As arestas devem ser informada no modelo: a1(J-C), a2(C-E), a3(C-E)")
    ares = input("Digite as Arestas do Grafo >>>  ")
    ares = ares.split(", ")         # Separando a String de entrada em uma lista com cada Par de Aresta como elemento,

    try:
        for i in range(len(ares)):
            ares[i] = ares[i].replace(")","(")          # Uniformisando os parenteses na string, substituindo para um unico tipo "(" - Abre Parenteses -.
            ares[i] = ares[i].split("(")                # Separando a String que compõe as arestas pelo parenteses anteriormente uniformizado.
            g.adicionaAresta(ares[i][0], ares[i][1])    # Adicionando as Arestas na variavel " g "
            dic_aux[ares[i][0]] = ares[i][1]            # Criando Dicionario de Arestas

        return dic_aux
    except:
        print("Arestas invalidas! Formato não aceito ou não correspondentes aos vertices.")
        print("Digite no formato: 'a1(A-B), a2(C-D), a3(E-F)' - com conexões correspondentes aos vertices.")

def vertices_nao_Adjacentes():
    aux_n_adjacentes = []
    for i in range(len(matriz_de_adjc)):
        for e in range(i, len(matriz_de_adjc)):

            if i != e and matriz_de_adjc[i][e] == 0:
                aux_n_adjacentes.append(lista_vertices[i] + '-' + lista_vertices[e])

    return aux_n_adjacentes

def VerifyAres(S, DicA = {}):
    cont = 0
    for i in DicA.keys():
        if DicA[i] == S:
            cont += 1

    return cont

def matriz_adjacencia(V = [], D = {}):
    matriz = []
    aux = []
    for i in range(len(V)):
        for e in range(len(V)):
            S = V[i] + '-' + V[e]
            aux.append(VerifyAres(S, D))

        matriz.append(aux)
        aux = []

    return matriz

def procura_aresta_insidente(v = ''):
    aux = []
    for i in dicionario_arestas.keys():
        if v == dicionario_arestas[i][0] or v == dicionario_arestas[i][2]:
            aux.append(i)
    return aux

def Grafo_Completo():
    for i in range(len(matriz_de_adjc)):
        for e in range(len(matriz_de_adjc[i])):
            if ( (i != e) and (matriz_de_adjc[i][e] == 0 and matriz_de_adjc[e][i] == 0) ):
                return False
    return True

def arestas_paralelas():
    for i in range(len(matriz_de_adjc)):
        for e in range(len(matriz_de_adjc[i])):
            if matriz_de_adjc[i][e] == 2:
                return True
            elif matriz_de_adjc[i][e] > 0 and matriz_de_adjc[e][i] > 0 and i != e:
                return True
    return False

def adjc_ele_mesmo2(M):
    cont = 0
    for i in range(len(M)):

        if (M[i][cont] > 0):
            return True

        cont += 1;

    return False

def grau_do_vertice(v):
    cont_grau = 0
    for i in range(len(lista_vertices)):
        if lista_vertices[i] == v:

            for e in range(len(matriz_de_adjc[i])):
                if matriz_de_adjc[i][e] > 0:
                    cont_grau += matriz_de_adjc[i][e]
                if matriz_de_adjc[e][i] > 0:
                    cont_grau += matriz_de_adjc[e][i]

            return cont_grau

    return 0

def imprime():
    print(g,'\n')
    print("A) - Vertives não adjacentes >>> ", end=' ')
    for i in range(len(vert_nao_adjacentes)):
        if i < len(vert_nao_adjacentes) -1:
            print(vert_nao_adjacentes[i], end=', ')
        else:
            print(vert_nao_adjacentes[i])
    print("B) - Há vertices adjacentes a ele mesmo? >>> ", adjc_ele_mesmo2(matriz_de_adjc))
    print("C) - Existem Arestas Paralelas ? >>> ", arestas_paralelas())
    print("D) - Grau do Vertice " + vert + " >>> ", grau_do_vertice(vert))
    print("E) - Arestas insidentes no vertice ", vert_inside, ' >>> ', end='')
    for i in range(len(InsideArestas)):
        if i < len(InsideArestas) -1:
            print(InsideArestas[i], end=' - ')
        else:
            print(InsideArestas[i],end='')
    print('')
    print('F) - O Grafo é completo ? >>> ', GrafoCompleto)
### DESAFIO ###

def ciclos_grafo(C = '', A = {}):

    if C.count(C[-1]) == 2:
        lista_de_ciclos.append(C)
        return C
    aux = []
    for i in A.keys():
        if A[i][0] == C[-1]:
            aux.append(A[i][2])
        if A[i][2] == C[-1]:
            aux.append(A[i][0])
    caminho = []
    for i in range(len(aux)):
        if C[-2:][0] != aux[i]:
            caminho.append(C + aux[i])

    for i in range(len(caminho)):
        ciclos_grafo(caminho[i], A)

def imprime_ciclos():

    for i in range(len(lista_de_ciclos)):
        if i % 2 == 0:
            cont = 0
            while (lista_de_ciclos[i][cont] != lista_de_ciclos[i][-1]):

                del lista_de_ciclos[i][cont]
                cont += 1

            for e in range(len(lista_de_ciclos[i])):
                if e < len(lista_de_ciclos[i]) -1:
                    print(lista_de_ciclos[i][e], end=' - ')
                else:
                    print(lista_de_ciclos[i][e])


g = Grafo() # Iniciando a variavel " g ", que representa um Grafo.

vert = 'C'
vert_inside = 'M'


lista_vertices = ent_vertices()
dicionario_arestas = ent_arestas()
matriz_de_adjc = matriz_adjacencia(lista_vertices, dicionario_arestas)
vert_nao_adjacentes = vertices_nao_Adjacentes()
InsideArestas = procura_aresta_insidente(vert_inside)
GrafoCompleto = Grafo_Completo()
for i in range(len(matriz_de_adjc)):
    print(matriz_de_adjc[i])
imprime()

### DESAFIO ###

lista_de_ciclos = []
ciclos_grafo('T', dicionario_arestas)
print(lista_de_ciclos)
print("DESAFIO : Há Ciclos no grafo ? >>>", end=' ')
if len(lista_de_ciclos) == 0:
    print(False)
else:
    print(True, end=' :> ')
    imprime_ciclos()


#   a1(J-C), a2(C-E), a3(C-E), a4(C-P), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
#   J, C, E, P, M, T, Z

# a1(J-C), a3(C-E), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
# a1(J-C), a3(C-E), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z), A10(J-J)
