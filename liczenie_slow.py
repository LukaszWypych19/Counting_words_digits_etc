# tekst = input('Napisz jakis wyraz lub tekst: ')

plik = open('wyniki_f1.txt')
czytaj = plik.read()
print(czytaj)
plik.close()



def ilosc_znakow():
    return len(czytaj)

def ilosc_slow():
    txt = len(czytaj.split())
    return txt

def ilosc_liter():
    slowa = 0

    for char in czytaj:
        char = char.lower()
        if char == ' ':
            slowa += 1
        # else:


print(f'W tym tekscie jest {ilosc_znakow()} znakow')
print(f'W tym tekscie jest {ilosc_slow()} słow')
print(f'W tym tekscie jest {ilosc_liter()} liter')

