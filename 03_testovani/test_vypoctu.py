"""Samostatný soubor s testy.

Takto je to nejlepší.
Je potřeba naimportovat funkce, které budem testovat a ty pak použít v testech.
"""

import pytest

from vypocty import odecti
from vypocty import secti


def test_scitani_stringu():
    assert secti('ahoj', ' svete') == 'ahoj svete'


def test_odcitani_stringu():
    with pytest.raises(TypeError):
        odecti('tohle', 'nepujde')
