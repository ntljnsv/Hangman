import random
from zborovi import listaZborovi


def zborZaBesilka():
    zbor = random.choice(listaZborovi)
    return zbor.upper()


def besilka(zbor):
    zavrsenZbor = '_' * len(zbor)
    pogoden = False
    obidi = 6
    pogodeniBukvi = []
    pogodeniZborovi = []
    print('Da igrame besilka!')
    print(prikaziBesilka(obidi))
    print(zavrsenZbor)
    print('\n')
    while not pogoden and obidi > 0:
        godenje = input('Pogodete bukva ili zbor ').upper()
        if len(godenje) == 1 and godenje.isalpha():
            if godenje in pogodeniBukvi:
                print('Veke ja pogodivte bukvata ', godenje)
            elif godenje not in zbor:
                print('Bukvata ', godenje, ' ne e vo zborot')
                obidi -= 1
                pogodeniBukvi.append(godenje)
            else:
                print('Bravo ', godenje, ' e bukva vo zborot!')
                pogodeniBukvi.append(godenje)
                zborLista = list(zavrsenZbor)
                linii = [i for i, letter in enumerate(zbor) if letter == godenje]
                # so enumerate() go dobivame brojot na elementi vo zbor i vrednosta na sekoj element
                for index in linii:
                    zborLista[index] = godenje
                zavrsenZbor = ''.join(zborLista)
                if '_' not in zavrsenZbor:
                    pogoden = True
        elif len(godenje) == len(zbor) and godenje.isalpha():
            if godenje in pogodeniZborovi:
                print('Veke go godevte zborot ', godenje)
            elif godenje != zbor:
                print(godenje, ' ne e baraniot zbor!')
                obidi -= 1
                pogodeniZborovi.append(godenje)
            else:
                pogoden = True
                zavrsenZbor = godenje
        else:
            print('Nevaliden obid')
        print(prikaziBesilka(obidi))
        print(zavrsenZbor)
        print('\n')
    if pogoden:
        print('Bravo! Go pogodivte zborot!')
    else:
        print('Zalam, nemate poveke obidi. Zborot bese', zbor)


def prikaziBesilka(obidi):
    faza = [
        """
        ------------
        |        |
        |        O
        |       \|/
        |        |
        |       / \\
        |
        -
        """,
        """
        ------------
        |        |
        |        O
        |       \|/
        |        |
        |       / 
        |
        -
        """,
        """
         ------------
         |        |
         |        O
         |       \|/
         |        |
         |        
         |
         -
        """,
        """
         ------------
         |        |
         |        O
         |        |/
         |        |
         |        
         |
         -
        """,
        """
         ------------
         |        |
         |        O
         |        |
         |        |
         |        
         |
         -
        """,
        """
         ------------
         |        |
         |        O
         |      
         |        
         |        
         |
         -
          """,
        """
         ------------
         |        |
         |        
         |      
         |        
         |        
         |
         -
          """
    ]
    return faza[obidi]


def main():
    zbor = zborZaBesilka()
    besilka(zbor)
    while input('Igraj povtorno? (DA/NE)').upper() == 'DA':
        zbor = zborZaBesilka()
        besilka(zbor)
if __name__ == '__main__':
    main()
# __name__ e specijalen vid promenliva koja go cuva imeto na module koj go koristime