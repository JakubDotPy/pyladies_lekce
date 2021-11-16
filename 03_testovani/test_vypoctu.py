import pytest

from vypocty import secti
from vypocty import odecti


def test_scitani_stringu():
    assert secti('ahoj', ' svete') == 'ahoj svete'


def test_odcitani_stringu():
    with pytest.raises(TypeError):
        odecti('tohle', 'nepujde')
