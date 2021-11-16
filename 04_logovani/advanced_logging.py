import logging
from log_config import setup_logging

# NOTE: basic logging
logging.basicConfig(
    filename='muj_vypis.log',
    # format='%(asctime)s %(module)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    )
log = logging.getLogger('root')

# NOTE: advanced logging
# setup_logging()
# log = logging.LoggerAdapter(logging.getLogger('basic'), {"sID": 'script'.ljust(13)})


log.info('This is log from my script.')
log.info('Now I am ready to start.')


def division_function(a, b):
    log.info('Running division funciton.')
    log.debug(f'got {a=} and {b=}')
    result = None
    try:
        log.debug('dividing')
        result = a / b
    except:
        log.exception('dividing unsuccessfull')
    else:
        log.debug(f'result is {result}')
    finally:
        return result


log.info('I need to call the division function')
result_of_division = division_function(10, 3)

if result_of_division < 5:
    log.warning('!!! The division was too low !!!')
else:
    log.info('Everything in normal.')
