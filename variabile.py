#variabila = zona din memorie care tine date
#          = cutiuta in care punem valori

#am declarat si initializat variabila marca
marca_masina = 'Volvo'
model_masina = 'XC60'

#nu putem sa punem spatiu in numele variabilei
#o variabila incepe cu litera mica

#strongly typed - trebuie sa specificam tipul de variabila cu care lucram (in Java)
#loosely type = nu trebuie sa specificam tipurile de variabile (in Pyt)
#statement = propozitie

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

#suprascriere/overwritte
model_masina = 'XC60 facelift'
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

nume = 'Duca'
prenume = 'Andreea'
varsta = 22
print(prenume +' ' + nume)
print(f'Eu sunt {prenume}  {nume} si am varsta de {varsta} ani')
