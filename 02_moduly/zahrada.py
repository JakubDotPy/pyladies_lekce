import random

CLOVEK_HODINA_M2 = 1 / 60  # minuta
VELIKOST_ZAHRADY = 500  # m2

print('Importuji zahradu')


def posekat(pocet_lidi):
    """Spočítá, jak dlouho se bude sekat zahrada."""
    doba_sekani = (VELIKOST_ZAHRADY * CLOVEK_HODINA_M2) / pocet_lidi
    print(f'{pocet_lidi} lidi sekají zahradu {doba_sekani:.2f} hodin')


def zasadit_kytky(nazev, pocet):
    print(f'Sázím {nazev}')
    for _ in range(pocet):
        offset = random.randint(2, 50)
        print('X'.center(offset))
