def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):
        linha = []
        for j in range(n - i - 1):
            v = round(tabela[i][j] - tabela[i][j + 1], 2) 
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


def proximoA(grau, tabela):
    
    while grau > 0:

        resultado = tabela[grau-1][-1] - tabela[grau][-1]
 
        tabela[grau-1].append(resultado)

        grau -=1
        
    return resultado

        
def encontraLinhaValorIgual(diffs):
    for linha in diffs:
        if all(x == linha[0] for x in linha):
            return linha[0]
    


coeficientes = [2,-3,1,-5]
grau = len(coeficientes) - 1
eixo_x = [1,2,3,4,5,6,7,8,9]
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]

diffs = babbage(eixo_y)
valorIgual = encontraLinhaValorIgual(diffs)

# proximo = proximoA(diffs)


print(eixo_x)
print(eixo_y)
print("tabela de diferenças:")
for c, linha in enumerate(diffs):
    print(f"nível {c}: {linha}")
# print(f"Próximo valor estimado na sequência: {proximo}")

print("proximo valor sera de:", proximoA(grau, diffs))