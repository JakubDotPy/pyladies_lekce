"""Tento modul spusťte pro ukázku pokročilého logování."""

import logging

from log_config import setup_logging

# NOTE: nastavení logování
setup_logging()
log = logging.LoggerAdapter(logging.getLogger('basic'), {"sID": 'script'.ljust(13)})

log.info('Toto je log z mého skriptu.')
log.info('Nyní mohu začít')


def funkce_deleni(a, b):
    log.debug('Spoustim delici funkci.')
    log.debug(f'dostal jsem a={a} a b={b}')
    vysledek = None
    try:
        log.debug('delim')
        vysledek = a / b
    except:
        log.exception('deleni se nepovedlo')
    else:
        log.debug(f'vysledek je {vysledek}')
    finally:
        return vysledek


log.info('Nyni budu volat delici fukci.')
sada_cisel = [
    (10, 3),
    (20, 4),
    (15, 0),
    (20, 10),
    ]

for pokus, cisla in enumerate(sada_cisel):
    log.info('-' * 50)
    log.info(f'{pokus}. pokus')
    vysledek_deleni = funkce_deleni(*cisla)
    log.info(f'vysledek je {vysledek_deleni}')

    if not vysledek_deleni:
        log.error('nedostali jsme zadny vysledek')
        continue

    if vysledek_deleni < 5:
        log.warning('!!! vysledek byl prilis nizky !!!')
    else:
        log.info('vse v poradku')

log.info('Konec skriptu.')
