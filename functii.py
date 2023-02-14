'''
Functie = logica delimitata care poate fi refolosita
          o f simpla care ne printeaza ceva pe ecran
          nu ne da nici un raspuns ( nu are return )
          nu are parametrii
          nu putem folosi spatii in nume
'''

def printGreeting():
    print('Buna ziua! Bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume} ! ')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
       return 3.14

 #exercitiu
 #daca pers e majora, altfel false

def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

#zona de apelare (desktop)

printGreeting()
printGreeting()
printGreetingByName('Duca', 'Andreea')
printGreetingByName('Duca', 'Dan')
printGreetingByName('Duca', 'Anda')
print(mediaNr(3,3,4))
print(piValue())

#se ia vasrta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat, bine ai venit in aplicatie!')
else:
    print('Nu ai varsta minima necesara!')

    #OOP - VARIABILE SI FUNCTII
    '''
    variabile => atribute, proprietati sau fields
    functii => metode
    '''