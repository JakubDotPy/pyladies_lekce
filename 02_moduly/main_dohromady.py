import random

ZDI = r"""
|         |
| [I] [I] |
|    __   |
|   |  |  |
|   |  |  |
"""
VELIKOST_ZAHRADY = 500  # m2
STRECHA = r"""
     A     
    / \ H
   /   \H
  /     \
 /       \ 
"""
CLOVEK_HODINA_M2 = 1 / 60  # minuta
ZAKLADY = r"""
===========
"""


def posekat(pocet_lidi):
    """Spočítá, jak dlouho se bude sekat zahrada."""
    doba_sekani = (VELIKOST_ZAHRADY * CLOVEK_HODINA_M2) / pocet_lidi
    print(f'{pocet_lidi} lid sekají zahradu {doba_sekani:.2f} hodin')


posekat(pocet_lidi=3)


def postavit_strechu():
    print(STRECHA)


postavit_strechu()


def uklidit_garaz():
    mysi = random.randint(0, 50)
    print(f'Vyhnal jsem {mysi} myší!!!')


def postavit_zaklady():
    print(ZAKLADY)


def postavit_zdi():
    print(ZDI)


def roztridit_sroubky(pocet, hromadky):
    print(f'{pocet} sroubku jsem dal na {hromadky} hromádky.')
    print(f'V každé je {pocet // hromadky} šroubků.')


roztridit_sroubky(pocet=200, hromadky=8)


def zasadit_kytky(nazev, pocet):
    print(f'Sázím {nazev}')
    for _ in range(pocet):
        offset = random.randint(2, 50)
        print('X'.center(offset))


postavit_zdi()
postavit_zaklady()
zasadit_kytky(nazev='kopretiny', pocet=20)
