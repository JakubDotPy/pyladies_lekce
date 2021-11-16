import logging.config
import os

CURRENT_DIR = os.getcwd()
os.makedirs(CURRENT_DIR + r'\logs', exist_ok=True)

COMPUTERNAME = 'PLZC01234'

LOG_CONF = {
    'version'   : 1,
    'formatters': {
        'file_form'   : {
            'format': '[%(sID)-13s] %(asctime)s - %(levelname)-8s - %(funcName)-22s - %(message)s'
            },
        'console_form': {
            'format': '[%(sID)-13s] %(levelname)-8s - %(message)s'
            },
        },
    'handlers'  : {
        'console_hand' : {
            'class'    : 'logging.StreamHandler',
            'stream'   : 'ext://sys.stdout',
            'level'    : 'INFO',
            'formatter': 'console_form',
            },
        'file_hand_rot': {
            'class'      : 'logging.handlers.RotatingFileHandler',
            'filename'   : os.path.join(CURRENT_DIR, 'logs', COMPUTERNAME + '.log'),
            'maxBytes'   : 3_145_728,  # 3MB
            'backupCount': 5,  # five files with log backup
            'level'      : 'DEBUG',
            'encoding'   : 'utf-8',
            'formatter'  : 'file_form',
            },
        'file_err_hand': {
            'class'    : 'logging.FileHandler',
            'filename' : os.path.join(CURRENT_DIR, 'logs', COMPUTERNAME + '_ERROR.log'),
            'level'    : 'WARNING',
            'encoding' : 'utf-8',
            'formatter': 'file_form',
            },
        },
    'loggers'   : {
        'basic': {
            'handlers': ['console_hand', 'file_hand_rot', 'file_err_hand'],
            'level'   : 'DEBUG',
            }
        }
    }


def setup_logging():
    logging.config.dictConfig(LOG_CONF)
    log = logging.LoggerAdapter(logging.getLogger('basic'), {"sID": 'logging_setup'})
    log.info('Logging was set up.')
