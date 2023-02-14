piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else

# daca nr este par printam acest lucru, altfel printam impar
nr = 1
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? rest 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('nr pozitiv')
else:
    print('nr nu este pozitiv')

'''if,else if, else
cum ne saluta robotelul in functie de ora?
luam date de la tastatura
ne asiguram ca sunt transformate din str in int'''

ora = int(input('Introdu ora'))
user = input('Introdu numele tau')
if ora < 0:
    print('ora negativa. Introduceti o ora in intervalul 00-24')
elif ora <= 11:
    print('Buna dimineata,', user, '!')
elif ora <= 18:
    print('Buna ziua', user, '!')
elif ora <= 21:
    print('Buna seara', user, '!')
elif ora <= 24:
    print('Noapte buna', user, '!')
else:
    print('ora invalida. ora mai mare decat 24')

#CTRL + / = se comenteaza/decomenteaza mai multe linii de cod
# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('Meniu principal')
elif optiunea == 1:
    print('ati ales lb romana')
elif optiunea == 2:
    print('ati ales lb engleza')
else:
    print('Nr incorect, mai incearca')