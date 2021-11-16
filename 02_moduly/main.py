# TODO: vysvětlit různé druhy importu
from dum import postavit_strechu
from dum import postavit_zdi
from dum import postavit_zaklady

from garaz import *

import zahrada

postavit_strechu()
postavit_zdi()
postavit_zaklady()

roztridit_sroubky(pocet=200, hromadky=8)

zahrada.posekat(pocet_lidi=3)
zahrada.zasadit_kytky(nazev='kopretiny', pocet=20)


"""
Úkol: 
   Vytvoř si moduly kuchyn.py a obyvak.py
   Do každého z nich přidej nějakou funkci, která by se tam mohla provést.
   
   Poté vytvoř modul main.py a v něm funkce naimportuj a zavolej.
"""