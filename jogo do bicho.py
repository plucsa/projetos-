inicio = 1
fim = 101
passo = 1
lista = list(range(inicio, fim, passo))
def ListasMenores (lista,n):
    for i in range (0,len(lista), n):
        yield lista[i:i + n]
ListasDivididas = list(ListasMenores(lista, 4))
print(ListasDivididas)
v = float(input('digite valor da aposta(v): '))
n = float(input('digite valor milhar(n): '))
m = float(input('digite valor sorteado(m): '))
if n % 10000 == m % 10000:
    v = v * 3000.00
elif n % 1000 == m % 1000:
    v = v * 500
elif n % 100 == m % 100:
    v = v * 50
elif n % 100 and m % 100 in ListasDivididas:
    v = v * 16
else:
    v = v * 00
print('{:.2f}'.format(v))
