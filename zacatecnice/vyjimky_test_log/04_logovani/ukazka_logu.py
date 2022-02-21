import logging

# základní nastavení logování

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] - %(message)s',  # log format má speciální způsob zápisu
    handlers=[
        logging.FileHandler('muj_vypis.log'),  # toto přidá logování do souboru
        logging.StreamHandler()  # toto bude zapisovat do konzole (jako print)
        ]
    )

# pomocí log.info, log.debug ... pak zapisuji
log = logging.getLogger(__name__)


def funkce_s_logy():
    """Tato funkce počítá a hezky informuje pomocí logování."""

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


print('-' * 50, '\n', funkce_s_logy.__doc__)
funkce_s_logy()
