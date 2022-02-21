def funkce_bez_printu():
    """Tato funkce počítá, ale neinformuje o mezivýsledcích."""

    cislo = int(input("Zadej číslo: "))
    cislo = cislo + 1
    cislo = cislo ** 2
    cislo = cislo - 5
    print("Výsledek je:", cislo)


print('-' * 50, '\n', funkce_bez_printu.__doc__)
funkce_bez_printu()


def funkce_s_printy():
    """Tato funkce počítá, a informuje pomocí printů."""
    print("Načítám číslo od uživatele")
    cislo = int(input("Zadej číslo: "))
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


print('-' * 50, '\n', funkce_s_printy.__doc__)
funkce_s_printy()
