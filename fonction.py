import time

def chrono(seconde):
    """le paramétre seconde sera le nombre de seconde d'intervale"""
    temps = 0

    while True:
        debut = time.time()
        time.sleep(seconde)
        fin = time.time()
        temps += fin - debut
        print(temps)
        