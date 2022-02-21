""" Úkol: uživatel zadá číslo a my vypíšeme, kolik je 10 / číslo.

Spuštění celého souboru bude postupně spouštět všechny možnosti.
"""


# Jak by se to dělat nemělo
def zadej_cislo_nejhur():
    """Tato funkce se ptá uživatele na číselný vstup.

    Nijak ale neošetřuje výjimky.
    Pokud uživatel zadá špatné číslo, program spadne.
    """
    return float(input('Zadej cislo větší než 0 prosim: '))


# vytiske čáru, novou řádku a dokumentaci funkce
# nazev_funkce.__doc__ nám dá její dokumentační komentář
# (to je ten text hned pod názvem funkce v trojitých "
print('-' * 50, '\n', zadej_cislo_nejhur.__doc__)

# A doufali, že uživatel zadá číslo...
cislo = zadej_cislo_nejhur()
print(f'10 / {cislo} = {10 / cislo}')


# ------------------------------------------------------------------------------

# Ošetřivání pomocí ifů.
# Ale nefunguje s floaty...
# Co když zkusíme zadat desetinne místo?
def zadej_cislo_postaru():
    """Tato funkce se ptá uživatele na číselný vstup.

    Pokusí se zkontrolovat, zda vstup obsahuje jen čísla.
    Nefunguje s desetinnými čísly.
    """
    while True:
        # vezmeme si hodnotu tak, jak je, jako string
        hodnota_od_uzivatele = input('Zadej prosím číslo: ')

        # zkusíme, jestli je ve tvaru čísla
        if hodnota_od_uzivatele.isnumeric():
            cislo = float(hodnota_od_uzivatele)

            # zkontrolovat jestli je > 0
            if cislo > 0:
                return cislo
            else:
                print('Musíš zadat číslo které není 0!')
                continue
        else:
            print('Nezadal jsi číslo.')


print('-' * 50, '\n', zadej_cislo_postaru.__doc__)
cislo = zadej_cislo_postaru()
print(f'10 / {cislo} = {10 / cislo}')

# ------------------------------------------------------------------------------

print(' ukázka vyjimek '.center(50, '-'))

# Nastupují výjimky

# Pro úplnost a spokojenost IDE musíme na chvíli vypnout kontrolu pořadí výjimek
# noinspection PyExceptClausesOrder
try:

    print('V tomto bloku očekávám, že může nasta výjimka.')

except ValueError:
    print('Tohle se provede, pokud nastane ValueError')
except NameError:
    print('Tohle se provede, pokud nastane NameError')
except Exception:
    print('Tohle se provede, pokud nastane jiná chyba')
    # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
except TypeError:
    print('Tohle se neprovede nikdy')
    # ("except Exception" výše ošetřuje i TypeError; sem se Python nedostane)
else:
    print('Tohle se provede, pokud chyba nenastane')
finally:
    print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')

print(' konec ukázky vyjimek '.center(50, '-'))


# ------------------------------------------------------------------------------


def zadej_cislo_lepe():
    """Tato funkce se ptá uživatele na číselný vstup.

    Ošetřuje vstup pomocí try-except.
    """
    while True:
        # rovnou zkusím udelat to, co potřebuji
        try:
            # ale co když se staně něco nečekaného?
            return float(input('Zadej cislo: '))
        except ValueError:
            # Uživatel nezadal číslo
            print('Nezadal jsi číslo')


print('-' * 50, '\n', zadej_cislo_lepe.__doc__)

while True:
    try:
        cislo = zadej_cislo_lepe()
        print(f'10 / {cislo} = {10 / cislo}')
        break
    except ZeroDivisionError:
        print('Musíš zadat číslo které není 0!')


# ------------------------------------------------------------------------------


def spocti_vysledek():
    """Tato funkce spočítá 10 / vstup uživatele.

    Ošetřuje vstup pomocí try-except-else-finally.
    """

    # pokoušíme se udělat operaci
    try:
        # vezmeme si syrový vstup ve formě textu
        vstup_od_uzivatele = input('Zadej cislo: ')
        cislo = float(vstup_od_uzivatele)
        vysledek = 10 / cislo

    # něco se nepovedlo
    except ValueError:
        # Uživatel nezadal číslo
        print('Nezadal jsi číslo')

    except ZeroDivisionError:
        # uživatel zadal nulu
        print('Musíš zadat číslo které není 0!')

    else:
        print('Vše v pořádku')
        print(f'Výsledek je {vysledek}')

    finally:
        print('Děkuji že jste použili naše dělení.')


print('-' * 50, '\n', spocti_vysledek.__doc__)
spocti_vysledek()


# ------------------------------------------------------------------------------

# Vyvolání své vlastní výjimky.


def je_liche(cislo):
    return cislo % 2 == 1


def delim_jen_suda_cisla():
    """Funkce, která dělí jen sudá čísla."""

    try:
        prvni_cislo = int(input("Zadej první číslo: "))
        druhe_cislo = int(input("Zadej druhé číslo: "))

        if je_liche(prvni_cislo) or je_liche(druhe_cislo):
            raise ArithmeticError

        vysledek = prvni_cislo / druhe_cislo

    except ZeroDivisionError:  # NOTE: pořadí výjimek je důležité, neprohodit
        print('Nedělím nulou.')
    except ArithmeticError:  # NOTE: pořadí výjimek je důležité, neprohodit
        print('Dělím jen sudá čísla.')

    except ValueError:
        print('Dělím jen čísla.')
    else:
        print(f'Výsledek je: {vysledek}')
    finally:
        print('Děkuji za použití.')


print('-' * 50, '\n', delim_jen_suda_cisla.__doc__)
delim_jen_suda_cisla()

"""
Úkol: 
   Napiš funkci, která načte text ze souboru a ten vypíše.
   V případě, že soubor neexituje, vypíše "Soubor neexistuje."
   Použij blok try-except 
   (podívej se do taháku, kterou vyjimku bude nejlepší zachytit)
"""

print(' řešení domácího úkolu '.center(50, '-'))


# Řešení:

def precti_soubor(nazev):
    try:
        with open(nazev, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Soubor neexistuje.')


precti_soubor('neexistujici.txt')
"""
Bonusový Úkol:
   Projdi svůj kód a najdi pasáž, která by se dala pomocí try-except vylepšit.
   Prober s koučem.
"""
