# Úkol: uživatel zadá číslo a my vypíšeme, kolik je 10 / číslo


# Jak by se to dělat nemělo
def zadej_cislo_nejhur():
    """Tato funkce se ptá uživatele na číselný vstup.

    Nijak ale neošetřuje výjimky.
    """
    return float(input('Zadej cislo větší než 0 prosim: '))


# A doufali, že uživatel zadá číslo...
cislo = zadej_cislo_nejhur()
print(f'10 / {cislo} = {10 / cislo}')


# ------------------------------------------------------------------------------

# def zadej_cislo_postaru():
#     """Tato funkce se ptá uživatele na číselný vstup.
#
#     Pokusí se zkontrolovat, zda vstup obsahuje jen čísla.
#     """
#     while True:
#
#         # vezmeme si hodnotu tak, jak je, jako string
#         hodnota_od_uzivatele = input('Zadej prosím číslo: ')
#
#         # zkusíme, jestli je ve tvaru čísla
#         if hodnota_od_uzivatele.isnumeric():
#             cislo = float(hodnota_od_uzivatele)
#
#             # zkontrolovat jestli je > 0
#             if cislo > 0:
#                 return cislo
#             else:
#                 print('Musíš zadat číslo které není 0!')
#                 continue
#
#         else:
#             print('Nezadal jsi číslo.')
#
#
# cislo = zadej_cislo_postaru()
# print(f'10 / {cislo} = {10 / cislo}')


# Ale nefunguje s floaty...
# Co když zkusíme zadat desetinne místo?

# ------------------------------------------------------------------------------

# Nastupují výjimky

# try:
#     ...
# except ValueError:
#     print('Tohle se provede, pokud nastane ValueError')
# except NameError:
#     print('Tohle se provede, pokud nastane NameError')
# except Exception:
#     print('Tohle se provede, pokud nastane jiná chyba')
#     # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
# except TypeError:
#     print('Tohle se neprovede nikdy')
#     # ("except Exception" výše ošetřuje i TypeError; sem se Python nedostane)
# else:
#     print('Tohle se provede, pokud chyba nenastane')
# finally:
#     print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')

# ------------------------------------------------------------------------------

# def zadej_cislo_lepe():
#     """Tato funkce se ptá uživatele na číselný vstup.
#
#     Ošetřuje vstup pomocí try-except.
#     """
#     while True:
#
#         # rovnou zkusím udelat to, co potřebuji
#         try:
#             return float(input('Zadej cislo: '))
#
#         # ale co když se staně něco nečekaného?
#
#         except ValueError:
#             # Uživatel nezadal číslo
#             print('Nezadal jsi číslo')
#
#
# while True:
#     try:
#         cislo = zadej_cislo_lepe()
#         print(f'10 / {cislo} = {10 / cislo}')
#         break
#     except ZeroDivisionError:
#         print('Musíš zadat číslo které není 0!')


# ------------------------------------------------------------------------------


# def spocti_vysledek():
#     """Tato funkce spočítá 10 / vstup uživatele.
#
#     Ošetřuje vstup pomocí try-except-else-finally.
#     """
#
#     # pokoušíme se udělat operaci
#     try:
#         # vezmeme si syrový vstup ve formě textu
#         vstup_od_uzivatele = input('Zadej cislo: ')
#         cislo = float(vstup_od_uzivatele)
#         vysledek = 10 / cislo
#
#     # něco se nepovedlo
#     except ValueError:
#         # Uživatel nezadal číslo
#         print('Nezadal jsi číslo')
#
#     except ZeroDivisionError:
#         # uživatel zadal nulu
#         print('Musíš zadat číslo které není 0!')
#
#     else:
#         print('Vše v pořádku')
#         print(f'Výsledek je {vysledek}')
#
#     finally:
#         print('Děkuji že jste použili naše dělení.')
#
#
# spocti_vysledek()

# ------------------------------------------------------------------------------

# Vyvolání své vlastní výjimky.


# def je_liche(cislo):
#     return cislo % 2 == 1
#
#
# def delim_jen_suda_cisla():
#     """Funkce, která dělí jen sudá čísla."""
#
#     try:
#         prvni_cislo = int(input("Zadej první číslo: "))
#         druhe_cislo = int(input("Zadej druhé číslo: "))
#
#         if je_liche(prvni_cislo) or je_liche(druhe_cislo):
#             raise ArithmeticError
#
#         vysledek = prvni_cislo / druhe_cislo
#
#     except ZeroDivisionError:  # TODO: ukázat, že na pořadí záleží
#         print('Nedělím nulou.')
#     except ArithmeticError:  # TODO: ukázat, že na pořadí záleží
#         print('Dělím jen sudá čísla.')
#
#     except ValueError:
#         print('Dělím jen čísla.')
#     else:
#         print(f'Výsledek je: {vysledek}')
#     finally:
#         print('Děkuji za použití.')
#
#
# delim_jen_suda_cisla()
"""
Úkol: 
   Napiš funkci, která načte text ze souboru a ten vypíše.
   V případě, že soubor neexituje, vypíše "Soubor neexistuje."
   Použij blok try-except 
   (podívej se do taháku, kterou vyjimku bude nejlepší zachytit)
"""
# Řešení:
#
# def precti_soubor(nazev):
#     try:
#         with open(nazev, 'r') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('Soubor neexistuje.')
"""
Bonusový Úkol:
   Projdi svůj kód a najdi pasáž, která by se dala pomocí try-except vylepšit.
   Prober s koučem.
"""