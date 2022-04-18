## vyjimky

- projet postupně celý notebook

## moduly

### Příklad s barákem

- ukázat [main dohromady](02_moduly/main_dohromady.py)
- projít rozdělení na jednotlivé soubory
    - dum
    - garaz
    - zahrada
- ukazat uklizeno v [main](02_moduly/main.py)

### Problém cyklického importu

- spustit modul_a
- cyklický import s modul_b
- vysvětlit řešení
    - přidat třetí
    - import až na místě
    - `if __name__ == '__main__'`
- ukázat name main v [materiálech](https://naucse.python.cz/2022/plzen-jaro-2022/beginners/modules/)

## testování

- projit soubor vypocty.py
- pak ukázat jak by to bylo lepší se separátním modulem test_vypoctu.py

## logování

- projit ukazka_printu
- motivace - zároveň do souboru
- zmínit levely
- ukazat vylepšní v ukazka_logu
- nakonec ukázat advanced logging s log config