"""
in JAVA => MAP
map = o reprezentare de date in sistem cheie valoare
map nu este ordonat
ex: Gigel are la bac 10, dar Costel are nota 9
in PYT => DICT
"""
lista_goala = [0]
dict_gol = {}

# declaram si initializam un DICT
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam elemente/note
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori => .pop
note_elevi.pop('Gigel')
print(note_elevi.pop('Gigel', 'nu avem cheia'))
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())