from grafo import Grafo

## Função para entrada dos vertices ##
def ent_vertices():
    try:
        vert = input("Digite os Vertices do Grafo >>>  ")
        vert = vert.split(", ")  # Separando a String de entrada em uma lista com cada Vertices como elemento.

        for i in vert:
            g.adicionaVertice(i)  # Adicionando Vertices na variavel " g ".
        return vert

    except:
        print("Vertices invalidos! Formato não aceito.")
        print("Digite no formato: 'A, B, C, D'")

def ent_arestas():
    dic_aux = {}
    # print("As arestas devem ser informada no modelo: a1(J-C), a2(C-E), a3(C-E)")
    ares = input("Digite as Arestas do Grafo >>>  ")
    ares = ares.split(", ")  # Separando a String de entrada em uma lista com cada Par de Aresta como elemento,

    try:
        for i in range(len(ares)):
            ares[i] = ares[i].replace(")","(")  # Uniformisando os parenteses na string, substituindo para um unico tipo "(" - Abre Parenteses -.
            ares[i] = ares[i].split(
                "(")  # Separando a String que compõe as arestas pelo parenteses anteriormente uniformizado.
            g.adicionaAresta(ares[i][0], ares[i][1])  # Adicionando as Arestas na variavel " g "
            dic_aux[ares[i][0]] = ares[i][1]  # Criando Dicionario de Arestas

        return dic_aux
    except:
        print("Arestas invalidas! Formato não aceito ou não correspondentes aos vertices.")
        print("Digite no formato: 'a1(A-B), a2(C-D), a3(E-F)' - com conexões correspondentes aos vertices.")

def VerifyAres(S, DicA={}):
    cont = 0
    for i in DicA.keys():
        if DicA[i] == S:
            cont += 1

    return cont

def Nao_Adjacentes(V=[], A={}):
    NaoAdjc = []
    for i in range(len(V)):
        for e in range(i, len(V)):

            if V[i] != V[e]:
                StringAres = V[i] + '-' + V[e]
                Verify = VerifyAres(StringAres, A)

                if (Verify == 0):
                    NaoAdjc.append(StringAres)

    return NaoAdjc

def arestas_paralelas(V=[],A={}):
    for i in range(len(V)):
        for e in range(i, len(V)):

            if V[i] != V[e]:
                StringAres = V[i] + '-' + V[e]

                if VerifyAres(StringAres, A) == 2:
                    return True
    return False

def adjc_ele_mesmo(V=[], A={}):
    for i in range(len(V)):
        StringAres = V[i] + '-' + V[i]
        Verify = VerifyAres(StringAres, A)

        if Verify != 0:
            return True

    return False

def Grau_Vertice(v = '', A={}):
    cont = 0

    for i in A.keys():
        if v == A[i][0] or v == A[i][2]:
            cont += 1

    return cont

def Insidencia_Arestas(v = '', A={}):
    lista_ares_inside = []

    for i in A.keys():
        if A[i][0] == v or A[i][2] == v:
            lista_ares_inside.append(i)

    return lista_ares_inside

def Grafo_Completo(A=[]):
    if len(A) == 0:
        return True
    else:
        return False

def imprime():
    print(g,'\n')
    if len(NaoAdjcentes) == 0:
        print("A) - Todos os vertices são adjacentes!")
    else:
        print("A) - Vertices não adjacentes >>> ",end='')
        for i in range(len(NaoAdjcentes)):
            if i < len(NaoAdjcentes) - 1:
                print(NaoAdjcentes[i], end=', ')
            else:
                print(NaoAdjcentes[i])
    print("B) - Há vertices adjacentes a  ele mesmo? >>> ", AdjcEleMesmo)
    print("C) - Existem Arestas paralelas ? >>> ", arestas_paralelas(vertices, arestas))
    print("D) - Grau do vertice", vert, ">>> ", GrauVertice)
    print("E) - Arestas insidentes no vertice ", vert_inside, ' >>> ', end='')
    for i in range(len(InsideArestas)):
        if i < len(InsideArestas) - 1:
            print(InsideArestas[i], end=' - ')
        else:
            print(InsideArestas[i], end='')
    print('')
    print("F) - O Grafo é completo ? >>>", GrafoCompleto)

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
        if len(C) == 1:
            indice = -1
        else:
            indice = -2

        if C[indice] != aux[i]:
            caminho.append(C + aux[i])

    for i in range(len(caminho)):
        ciclos_grafo(caminho[i], A)

def modela_caminho_ciclos():
    lista_aux = []

    for i in range(len(lista_de_ciclos)):
        aux = ''
        dentro_do_laco = False

        for e in lista_de_ciclos[i]:
            if e == lista_de_ciclos[i][-1]:
                dentro_do_laco = True

            if dentro_do_laco == True:
                aux += e

        if aux not in lista_aux:
            lista_aux.append(aux)

    return lista_aux

def imprime_ciclos():

    for i in range(len(lista_ciclos_final)):
        if len(lista_ciclos_final[i]) == 2 or i % 2 == 0:

            for e in range(len(lista_ciclos_final[i])):

                if e < len(lista_ciclos_final[i]) -1:
                    print(lista_ciclos_final[i][e], end=' - ')
                else:
                    print(lista_ciclos_final[i][e],end=' / ')

g = Grafo()  # Iniciando a variavel " g ", que representa um Grafo.

vert = 'C'
vert_inside = 'M'

vertices = ent_vertices()
arestas = ent_arestas()

NaoAdjcentes = Nao_Adjacentes(vertices, arestas)
AdjcEleMesmo = adjc_ele_mesmo(vertices, arestas)
GrauVertice = Grau_Vertice(vert, arestas)
InsideArestas = Insidencia_Arestas(vert_inside, arestas)
GrafoCompleto = Grafo_Completo(NaoAdjcentes)

imprime()

### DESAFIO ###

lista_de_ciclos = []
ciclos_grafo('T', arestas)
lista_ciclos_final = modela_caminho_ciclos()

print("DESAFIO : Há Ciclos no grafo ? >>>", end=' ')
if len(lista_de_ciclos) == 0:
    print(False)
else:
    print(True, end=' :> ')
    imprime_ciclos()
print('\n\n')

#   a1(J-C), a2(C-E), a3(C-E), a4(C-P), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
#   J, C, E, P, M, T, Z

# a1(J-C), a3(C-E), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
# a1(J-C), a3(C-E), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z), A10(J-J)

## Grafo Completo, sem laços :
# a1(J-C), a2(C-E), a3(C-E), a4(C-P), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z), a10(J-E), a11(J-P), a12(J-M), a13(J-T), a14(J-Z), a15(C-Z), a16(E-P), a17(E-M), a18(E-T), a19(E-Z), a20(P-M), a21(P-T), a22(P-Z), a23(M-Z)

# a1(J-C), a3(C-E), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z), a10(J-E), a11(J-P), a12(J-M), a13(J-T), a14(J-Z), a15(C-Z), a16(E-P), a17(E-M), a18(E-T), a19(E-Z), a20(P-M), a21(P-T), a22(P-Z), a23(M-Z)