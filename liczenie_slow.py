# tekst = input('Napisz jakis wyraz lub tekst: ')

plik = open('wyniki_f1.txt')
czytaj = plik.read()
print(czytaj)
plik.close()

list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_marks = [' ', ',', '.', ':', '/']
def ilosc_znakow():
    return len(czytaj)

def ilosc_slow():
    txt = len(czytaj.split())
    return txt

def ilosc_liter():
    litera = 0
    for i in czytaj:
        if i not in list_of_marks:
            if i not in list_of_digits:
                litera += 1
    return litera

# funkcja licząca ile roznych cyfr pojawia sie w tekscie
def ilosc_roznych_cyfr():
    digit = 0
    for i in list_of_digits:
        if i in czytaj:
            digit += 1
    return digit

# funkcja licząca ile cyfr pojawia sie w tekscie
def ilosc_wszystkich_cyfr():
    digit = 0
    for i in czytaj:
        if i in list_of_digits:
            digit += 1
    return digit


print(f'W tym tekscie jest {ilosc_znakow()} znakow')
print(f'W tym tekscie jest {ilosc_slow()} słów')
print(f'W tym tekscie jest', ilosc_roznych_cyfr(), 'roznego rodzaju cyfr')
print(f'W tym tekscie jest', ilosc_wszystkich_cyfr(), 'cyfr')
print(f'W tym tekscie jest', ilosc_liter(), 'liter')
