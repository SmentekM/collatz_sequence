liczba = int(input('Podaj liczbę z zakresu od 1 do 100: '))
print(liczba, end=' ')
if liczba < 1 or liczba > 100:
    print('Podano liczbę z poza zakresu!')
else:
    while liczba > 1:
        if liczba % 2 == 0:
            liczba = int(liczba/2)
            print(f'{liczba}', end=' ')
        elif liczba % 2 != 0:
            liczba = int(3*liczba +1)
            print(f'{liczba}', end=' ')
