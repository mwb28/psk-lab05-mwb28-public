"""
Erzeuge eine Grafik einer Farbpalette
"""
from pytamaro.de import (Grafik, leere_grafik, neben, rechteck, rgb_farbe,
                         ueber, zeige_grafik, weiss)

GROESSE_FARBQUADRATE: int = 400
GROESSE_ABSTAND : int = 10
GROESSE_EINZEL_QUADRATE : float= GROESSE_FARBQUADRATE/ 8
FARBSCHRITTE : float = 255/8


def zeichne_farbverlauf_reihe(startfarbe_rot: int, startfarbe_gruen : int)-> Grafik:
    startfarbe_rot : int = startfarbe_rot % 256
    startfarbe_gruen : int = startfarbe_gruen % 256
    linie : Grafik = leere_grafik()
    for i in range(4):
        rechteck1 : Grafik= rechteck(GROESSE_EINZEL_QUADRATE,GROESSE_EINZEL_QUADRATE,rgb_farbe(startfarbe_rot,startfarbe_gruen,(2*i)*(FARBSCHRITTE)))
        rechteck2 : Grafik = rechteck(GROESSE_EINZEL_QUADRATE,GROESSE_EINZEL_QUADRATE,rgb_farbe(startfarbe_rot,startfarbe_gruen,(2*i+1)*(FARBSCHRITTE)))
        linie = neben (linie, neben(rechteck1, rechteck2))
    return linie

def zeichne_Quadrat(rotanteil : int)-> Grafik:
    rotanteil : int = rotanteil %256
    farbquadrat : Grafik = leere_grafik()
    for i in range (4):
        farbquadrat= ueber(farbquadrat, ueber(zeichne_farbverlauf_reihe(rotanteil,2*i*FARBSCHRITTE), zeichne_farbverlauf_reihe(rotanteil,(2*i+1)*FARBSCHRITTE)))
    return farbquadrat

def zeichne_quadrat_reihe()->Grafik:
    quadrat_spalte : Grafik= leere_grafik()
    abstand_quadrat : Grafik = rechteck(GROESSE_ABSTAND,GROESSE_FARBQUADRATE,weiss)
    for i in range(4):
        quadrat_links : Grafik = zeichne_Quadrat(2*i*FARBSCHRITTE)
        quadrat_rechts : Grafik= zeichne_Quadrat((2*i+1)*FARBSCHRITTE)
        if i < 3:
            quadrat_spalte= neben(quadrat_spalte,neben(quadrat_links,neben(abstand_quadrat,neben(quadrat_rechts,abstand_quadrat))))
        else:
            quadrat_spalte = neben(quadrat_spalte,neben(quadrat_links, neben(abstand_quadrat,quadrat_rechts)) )
        
    return quadrat_spalte


zeige_grafik(zeichne_quadrat_reihe())
