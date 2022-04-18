"""Všimněte si různých druhů importu a jejich použití."""

# Je možný, ale pak musíte volat pomocí názvu a tečky.
# řádek 20 a 21
import zahrada
# Tenhle je doporučený
from dum import postavit_strechu
from dum import postavit_zaklady
from dum import postavit_zdi
# Tenhle spíš nepoužívat
from garaz import *

postavit_strechu()
postavit_zdi()
postavit_zaklady()

roztridit_sroubky(pocet=200, hromadky=8)
uklidit_garaz()

zahrada.posekat(pocet_lidi=3)
zahrada.zasadit_kytky(nazev='kopretiny', pocet=20)

"""
Úkol: 
   Vytvoř si moduly kuchyn.py a obyvak.py
   Do každého z nich přidej nějakou funkci, která by se tam mohla provést.
   
   Poté vytvoř modul main.py a v něm funkce naimportuj a zavolej.
"""
