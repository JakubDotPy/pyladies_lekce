r"""
Modul s vypocty.

Funkce v tomto modulu budeme testovat pomocí knihovny pytest

\venv\Scripts\activate
python -m pip install pytest

"""

import pytest


def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def vydel(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


# ------------------------------------------------------------------------------

# def test_scitani():
#     assert secti(1, 1) == 2
#     assert secti(5, 2) == 7
#
#
# def test_odcitani():
#     assert odecti(1, 1) == 0
#     assert odecti(5, 2) == 3
#
#
# def test_deleni():
#     assert vydel(1, 1) == 1
#     assert vydel(6, 2) == 3
#     # assert vydel(10, 0) == 0
#
#
# def test_deleni_nulou():
#     with pytest.raises(ZeroDivisionError):
#         vydel(10, 0)

# ------------------------------------------------------------------------------

# @pytest.mark.parametrize(
#     ('a', 'b', 'expected'),
#     [
#         (1, 2, 3),
#         (3, 5, 8),
#         (10, 20, 30),
#         ]
#     )
# def test_scitani_parametr(a, b, expected):
#     assert secti(a, b) == expected

"""
Úkol: 
   Vytvoř funkci, která 
   dostane string, znak a index, od kterého doprava spočítá počet znaků.
   
   def pocitam_znaky(text, znak, index):
   
   vstup:    'aaaaabbbbbcccc' 'b' 7
   
   příklad:  'aaaaabbb|bbcccc' 'b' 7 -> 2
   příklad:  'aaaaabbbb|bcccc' 'b' 8 -> 1
   příklad:  'aaaaabbbb|bcccc' 'c' 8 -> 4
   příklad:  'aaaaab|bbbbcccc' 'a' 5 -> 0
   příklad:  'aa|aaabbbbbcccc' 'a' 1 -> 3
   
   Pokud uživatel zadá index mimo text, funkce vyhodí IndexError.

Bonus: použij TDD (napiš si první test)
"""


# Řešení:

#
# def pocitam_znaky(text, znak, index):
#     if not 0 < index < len(text):
#         raise IndexError
#     # NOTE: pozor na jednicku
#     return text[index + 1:].count(znak)


# def test_pocitani_znaku():
#     assert pocitam_znaky('aaaaabbbbbcccc', 'b', 7) == 2
#     assert pocitam_znaky('aaaaabbbbbcccc', 'b', 8) == 1
#     assert pocitam_znaky('aaaaabbbbbcccc', 'c', 8) == 4
#     assert pocitam_znaky('aaaaabbbbbcccc', 'a', 5) == 0
#     assert pocitam_znaky('aaaaabbbbbcccc', 'a', 1) == 3
#
#     # neexistujici znak!
#     assert pocitam_znaky('aaaaabbbbbcccc', 'h', 5) == 0
#
#     with pytest.raises(IndexError):
#         assert pocitam_znaky('asdf', 'a', -1)
#         assert pocitam_znaky('asdf', 'a', 20)

# parametrizovany
# @pytest.mark.parametrize(
#     ('text', 'znak', 'index', 'expected'),
#     [
#         ('aaaaabbbbbcccc', 'b', 7, 2),
#         ('aaaaabbbbbcccc', 'b', 8, 1),
#         ('aaaaabbbbbcccc', 'c', 8, 4),
#         ('aaaaabbbbbcccc', 'a', 5, 0),
#         ('aaaaabbbbbcccc', 'a', 1, 3),
#         ]
#     )
# def test_pocitani_znaku(text, znak, index, expected):
#     assert pocitam_znaky(text, znak, index) == expected
