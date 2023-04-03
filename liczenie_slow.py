# tekst = 'niespodzianka dupa dom kabaretdqwgeg'
tekst = input('Napisz jakis wyraz lub tekst: ')
def ilosc_znakow():
    return len(tekst)

def ilosc_slow():
    txt = len(tekst.split())
    return txt

print(f'W tym tekscie jest {ilosc_znakow()} znakow')
print(f'W tym tekscie jest {ilosc_slow()} słow')

