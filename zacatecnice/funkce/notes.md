# Opakovani cyklu

### Nasobilka

#### Dobře:
```python
pocet_radku = 5
pocet_sloupcu = 10
for radek in range(pocet_radku):
    for sloupec in range(pocet_sloupcu):
        print(radek * sloupec, end=' ')
    print()
```
#### Lépe:
```python
cisla = 5
nasobky = 10
for cislo in range(cisla):
    for nasobek in range(nasobky):
        print(cislo * nasobek, end=' ')
    print()
```

### Čtverec
```python
pocet_radku = 5
pocet_sloupcu = 5 

for cislo_radku in range(pocet_radku):
    for cislo_sloupce in range(pocet_sloupcu):
        
        # pokud jsme uvnitr ctverce, tzn. vypiseme mezeru
        if 0 < cislo_radku < pocet_radku - 1 and 0 < cislo_sloupce < pocet_sloupcu - 1:
            print('  ', end='')

        # jinak jsme na okraji, vypiseme 'X'
        else:
            print('X ', end='')
    print()
```

# Debug
ukázat ?


# Funkce

- [funkce](https://naucse.python.cz/2022/plzen-jaro-2022/beginners/functions/)
- [definice funkcí](https://naucse.python.cz/2022/plzen-jaro-2022/beginners/def/)
