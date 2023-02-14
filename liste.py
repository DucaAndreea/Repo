# listele in python pot sa cuprinda elemente de tipuri DIFERITE
# au dimensiune DINAMICA

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[0])
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')
print(fructe)

# suprascriem un element
fructe[0] = 'para'
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element (POP)
last = fructe.pop()
print('ultimul element din lista este:', last)
print('lista este:', fructe)

#de cate ori apare un element?
print(fructe.count(3))

#extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

