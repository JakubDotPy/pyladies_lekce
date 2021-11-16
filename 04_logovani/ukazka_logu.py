import logging

logging.basicConfig(
    filename='muj_vypis.log',
    # format='%(asctime)s %(module)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    )
log = logging.getLogger(__name__)


def funkce_s_logy():
    log.info('Nacitam cislo od uzivatele')
    cislo = int(input('Zadej cislo: '))
    log.info(f'Zadane cislo je: {cislo}')

    log.info(f'Pricitam jednicku')
    cislo = cislo + 1
    log.debug(f'Po pricteni jednicky je hodnota: {cislo}')

    log.info('Nasobim dvemi')
    cislo = cislo ** 2
    log.debug(f'Po vynasobeni dvemi je hodnota: {cislo}')

    log.info('Odecitam petku')
    cislo = cislo - 5
    log.debug(f'Po odecteni 5 je vysledek: {cislo}')

    print(f'Vysledek je: {cislo}')


funkce_s_logy()
