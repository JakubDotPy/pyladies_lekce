def funkce_bez_printu():
    cislo = int(input("Zadej číslo:"))
    cislo = cislo + 1
    cislo = cislo ** 2
    cislo = cislo - 5
    print("Výsledek je:", cislo)


def funkce_s_printy():
    print("Načítám číslo od uživatele")
    cislo = int(input("Zadej číslo:"))
    print("Zadané čislo je:", cislo)
    print("Přičítám jedničku")
    cislo = cislo + 1
    print("Po přičtení jedničky je hodnota:", cislo)
    print("Násobím dvěmi")
    cislo = cislo ** 2
    print("Po vynásobení dvěmi je hodnota:", cislo)
    print("Odečítám pětku")
    cislo = cislo - 5
    print("Po odečtení 5 je výsledek:", cislo)
    print("Výsledek je:", cislo)
    print("Konec programu")


