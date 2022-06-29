operadores = ["+","-","*","/"]
def welcome():
    print('''
Bem vindo a calculadora!
''')
def calculadora():
    operation = input('''
Digite a operação matemática que deseja concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')
    if operation in operadores:

        number_1 = int(input('digite seu primeiro numero: '))
        number_2 = int(input('digite seu segundo numero: '))

        # adição
        if operation == "+":
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)
        # Subtração
        elif operation == "-":
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)
        # Multiplicação
        elif operation == "*":
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)
        # Divisão
        elif operation == "/":
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        else:
            print('''escolha um operador valido''')
        again()
    else:
        print('''digite apenas operadores basicos!''')
        again()
def again():
    #função para realizar outro calculo
    calc_again = input('''deseja calcular de novo ? "s" para sim e "n" para não. ''')
    if calc_again.upper() == "S":
        calculadora()
    elif calc_again.upper() == "N":
        print('até a proxima!')
    else:
        again()
#chame calculadora() fora da função 
welcome()
calculadora()