from grafo import Grafo

## Função para entrada dos vertices ##
def ent_vertices():
    try:
        vert = "J, C, E, P, M, T, Z"
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
    ares = "a1(J-C), a2(C-E), a3(C-E), a4(C-P), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)"
    ares = ares.split(", ")         # Separando a String de entrada em uma lista com cada Par de Aresta como elemento,

    try:
        for i in range(len(ares)):
            ares[i] = ares[i].replace(")","(")          # Uniformisando os parenteses na string, substituindo para um unico tipo "(" - Abre Parenteses -.
            ares[i] = ares[i].split("(")                # Separando a String que compõe as arestas pelo parenteses anteriormente uniformizado.
            g.adicionaAresta(ares[i][0], ares[i][1])    # Adicionando as Arestas na variavel " g "
            dic_aux[ares[i][0]] = ares[i][1]            # Criando Dicionario de Arestas
            lista_desafio.append(ares[i][1])
        return dic_aux
    except:
        print("Arestas invalidas! Formato não aceito ou não correspondentes aos vertices.")
        print("Digite no formato: 'a1(A-B), a2(C-D), a3(E-F)' - com conexões correspondentes aos vertices.")

def VerifyAres(S, DicA = {}):
    for i in DicA.keys():
        if DicA[i] == S:
            return True

    return False

def Nao_Adjacentes(V = [], A = {}):
    NaoAdjc = []
    for i in range(len(V)):
        for e in range(i, len(V)):

            if V[i] != V[e]:
                StringAres = V[i]
                StringAres += '-'
                StringAres += V[e]
                Verify = VerifyAres(StringAres, A)

                if (Verify == False):
                    NaoAdjc.append(StringAres)

    return NaoAdjc

def adjc_ele_mesmo(V = [], A = {}):
    for i in range(len(V)):
        StringAres = V[i]
        StringAres += "-"
        StringAres += V[i]

        Verify = VerifyAres(StringAres, A)

        if Verify == True:
            return Verify

    return Verify

def Grau_Vertice(v = '', A = {}):
    cont = 0

    for i in A.keys():
        if v == A[i][0] or v == A[i][2]:
            cont += 1

    return cont

def Insidencia_Arestas(v = '', A = {}):
    lista_ares_inside = []

    for i in A.keys():
        if A[i][0] == v or A[i][2] == v:
            lista_ares_inside.append(i)

    return lista_ares_inside

def Grafo_Completo(A = []):
    if len(A) == 0:
        return True
    else:
        return False

def imprime_nao_adjc(A= []):
    if len(A) != 0:
        print("\nVertices não adjacentes >>>", end=' ')
        for i in range(len(A)):
            print(A[i] + ',', end=' ')
        print('')
    else:
        print("Não há vertices não adjacentes")

def imprime_adjc_ele_mesmo(v):
    print("Há vertices adjacentes a  ele mesmo? >>>", end=' ')
    print(v)

def imprime_grau_vertice(v = '', grau = 0):
    print("Grau do Vertice " + v, end=' >>> ')
    print(grau)

def imprime_arestas_inside(a = '', A = []):
    print("Arestas Insidentes no vertice ", a, end=' >>> ')
    for i in range(len(A)):
        print(A[i] + ',', end=' ')
    print('')

def imprime_completo(c):
    print("O Grafo é completo ? >>> ",c)

def grafo_conexo(A = []):
    aux = A
    retorno = True
    for i in lista_desafio:

        del aux[0]
        for e in aux:
            if (i[0] == e[0]) or (i[0] == e[2]) or (i[2] == e[0]) or (i[2] == e[2]):
                retorno = False

        if retorno == True:
            return retorno
    
    return retorno
g = Grafo() # Iniciando a variavel " g ", que representa um Grafo.

vert = 'C'
vert_inside = 'M'
lista_desafio = []

vertices = ent_vertices()
arestas = ent_arestas()
NaoAdjcentes = Nao_Adjacentes(vertices, arestas)
AdjcEleMesmo = adjc_ele_mesmo(vertices, arestas)
GrauVertice = Grau_Vertice(vert, arestas)
InsideArestas = Insidencia_Arestas(vert_inside, arestas)
GrafoCompleto = Grafo_Completo(NaoAdjcentes)

print(g)
imprime_nao_adjc(NaoAdjcentes)
imprime_adjc_ele_mesmo(AdjcEleMesmo)
imprime_grau_vertice(vert, GrauVertice)
imprime_arestas_inside(vert_inside, InsideArestas)
imprime_completo(GrafoCompleto)

print(lista_desafio)
print(grafo_conexo(lista_desafio))
