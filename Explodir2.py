contador = 0
class No :
    lista = [x for x in range(100000)]
    proximo = None

if __name__  == "__main__" :
    raiz = No()
    temp = raiz
    while True:
        contador = contador + 1
        print("Executando consumir : ", contador)
        outro = No()
        temp.proximo = outro
        temp = outro