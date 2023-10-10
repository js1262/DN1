'''
Napišite funkcijo izpisi_trikotnik, ki sprejme celo število visina, ki predstavlja višino trikotnika. 
Funkcija naj vrne izpis trikotnika zvezdic v naslednji obliki:

Primer:

Če je visina enaka 5, naj funkcija izpiše:

*
**
***
****
*****

'''

def izpisi_trikotnik(v):
    for i in range(int(v)):
        print("*" * (i+1))

a = input('Vnesi višino trikotnika: ')
print(izpisi_trikotnik(a))