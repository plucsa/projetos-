from unicodedata import numeric
import webbrowser as wb
print("hello world!")
def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        idade = str(input(msg))  
        if idade.isnumeric():
            valor = int(idade)
        if valor >= 0 and valor < 120:
            ok = True
        else:
            print('\033[0;31mErro, digite uma idade valida entre 0 e 120!:\033[m')
        if ok :
            break
    return valor
Nom = str(input('digite seu nome: '))
N = Nom.strip()
while True:
    if all(c.isalpha() or c.isspace() for c in N) and len(N) > 3 and len(N) < 20 :
        break
    else:
        Nom = str(input('Seu nome só deve conter letras, e ter entre 3 a 20 letras! Digite novamente: '))
idade = LeiaInt('digite sua idade: ')
def search():
    if idade >= 18:
        print('seja bem vindo ao meu primeiro programa em python no VScode {}'.format(Nom))
        while True:
            x = int(input('oque deseja buscar hoje: 1-YouTube, 2-Web Whatsapp, 3-Liga Magic, 4-Google search, 5-exit:  '))
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
search()