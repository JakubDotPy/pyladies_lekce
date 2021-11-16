import time

while True:
    try:
        print('Mě nezastavíš.')
        time.sleep(1)
    except KeyboardInterrupt:
        print('Dobrý pokus :-)')
