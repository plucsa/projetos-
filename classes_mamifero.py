from hashlib import new


class mamifero(object):
    def __init__(self, cor_pelo_,genero, andar):
        '''classe para registrar um mamifero e suas caracteristicas'''
        self.cor = cor_pelo_
        self.genero = genero
        self.num_patas = andar
    def falar(self):
        print('olá, eu sou um mamifero e sei falar')
    def andar(self):
        print('estou andando sobre {} patas'.format(self.num_patas))
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('machos não podem amamentar')
            return
        else :
            print('amamentando o filhote')

#teste
rex = mamifero('preto','masculino',4)
rex.amamentar()

#classe para pessoas e polimorfismo
class pessoa(mamifero):
    def __init__(self, cor_pelo_, genero, andar,cabelo):
        super(pessoa,self).__init__(cor_pelo_, genero, andar)
        self.cabelo = cabelo
    def falar(self):
        print('olá, eu sou uma pessoa e sei falar')

#teste para pessoas
julia = pessoa('preta','feminino', 2 , 'loiro')
print(julia.cabelo)