""" POZOR, tento program nepůjde zastavit pomocí stisku ctrl+c !

K ukončení budete muset zavřít celý terminál nebo editor
"""

import time

while True:
    try:
        print('Mě nezastavíš.')
        time.sleep(1)
    except KeyboardInterrupt:
        print('Dobrý pokus :-)')
