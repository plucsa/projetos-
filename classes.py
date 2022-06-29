class cubo:
    def __init__(self, valor):
        self.x = valor
        print('objeto criado')
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return 'cubo calculado: ' + str(cubo)
teste = cubo(6)
c = teste.calcula_cubo()
print(c)