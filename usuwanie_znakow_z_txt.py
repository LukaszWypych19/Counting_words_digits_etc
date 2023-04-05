"""
plik = open('wyniki_f1.txt')
# czytaj = plik.read()

# print(czytaj)

czytaj = plik.read().replace(',', '')

print(czytaj)

list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_marks = [' ', ',', '<', '.', '>', ':', ';', '"', "'", '/', '-', '_', '|']

for i in czytaj:
    if i in list_of_digits:
        czytaj = czytaj.replace(i, '')
print(czytaj)
print(len(czytaj.split()))
"""
                    # funkcja usuwajaca znaki i litery z tekstu (plik)
                    # funkcja posiada zmienna - bez tego nie dziala

# tekst = input('Napisz jakis wyraz lub tekst: ')

plik = open('wyniki_f1.txt')
czytaj = plik.read()
print(czytaj)

# czytaj = plik.read().replace(',', '')
# print(czytaj)

list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_marks = [' ', ',', '<', '.', '>', ':', ';', '"', "'", '/', '-', '_', '|']
def ilosc_slow(czytaj):
    for i in czytaj:
        if i in list_of_digits:
            czytaj = czytaj.replace(i, '').replace(',', '')
    print(czytaj)
    print(len(czytaj.split()))

ilosc_slow(czytaj)