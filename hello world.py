from contextlib import redirect_stderr
from operator import truediv
import webbrowser as wb

print("hello world!")
Nom = str(input('digite seu nome: '))
idade = int(input('digite sua idade: '))
def search():
    if idade >= 18:
        print('seja bem vindo ao meu primeiro programa em python no VScode {}'.format(Nom))
        while True:
            search()
            print('oque deseja buscar hoje: 1-YouTube, 2-Web Whatsapp, 3-Liga Magic, 4-Google search, 5-exit ')
            x = int(input('>>>>>>>'))
            #condições
            if (x == 1):
                wb.open('https://www.youtube.com')
            elif (x == 2) :
                wb.open('https://web.whatsapp.com')
            elif (x == 3):
                wb.open('https://www.ligamagic.com.br/?view=home')
            elif (x == 4):
                wb.open('https://www.google.com.br')
            elif (x == 5) :
                input('aperte enter pra sair')
                break
            else:
                print('opção não aceita, digite novamente')
            print()
    else:
        print('infelizmente você não tem acesso nessa maquina devido a sua idade')