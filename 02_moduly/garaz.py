import random

print('Importuji garaz')


def uklidit_garaz():
    mysi = random.randint(0, 50)
    print(f'Vyhnal jsem {mysi} myší!!!')


def roztridit_sroubky(pocet, hromadky):
    print(f'{pocet} sroubku jsem dal na {hromadky} hromádky.')
    print(f'V každé je {pocet // hromadky} šroubků.')
