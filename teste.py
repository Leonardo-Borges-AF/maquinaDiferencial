def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):
        linha = []
        for j in range(n - i - 1):
            v = round(tabela[i][j] - tabela[i][j + 1], 4) 
            linha.append(v)
        tabela.append(linha)
    return tabela

def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while (i <= grau):
        soma += coeficientes[i] * (x ** (grau - i))
        i += 1
    return soma


def proximoA(grau, tabela, repete):
    aux = grau
    while repete > 0:
        grau = aux
        while grau > 0:
            resultado = round(tabela[grau-1][-1] - tabela[grau][-1],4)
            tabela[grau-1].append(resultado)
            grau -=1
        repete -=1
    grau = aux
    while grau > 0:
        resultado = round(tabela[grau-1][-1] - tabela[grau][-1],4)
        tabela[grau-1].append(resultado)
        grau -=1
    return tabela , resultado

def calculaRepeticao(eixo_x, numero):
    diferença = eixo_x[2] - eixo_x[1]
    repete = (numero - eixo_x[-1]) / diferença
    print(diferença)
    return repete

def encontraLinhaValorIgual(diffs):
    for linha in diffs:
        if all(x == linha[0] for x in linha):
            return linha[0]

coeficientes = [2,-3,2]
grau = len(coeficientes) - 1
eixo_x = [0.1,0.2,0.3,0.4]
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]

diffs = babbage(eixo_y)
valorIgual = encontraLinhaValorIgual(diffs)
repete = calculaRepeticao(eixo_x, 0.9)

print(eixo_x)
print(eixo_y)

tabela , resultado = proximoA(grau, diffs, repete)
print("tabela de diferenças:")
for c, linha in enumerate(tabela):
    print(f"nível {c}: {linha}")


print("proximo valor sera de:", resultado)