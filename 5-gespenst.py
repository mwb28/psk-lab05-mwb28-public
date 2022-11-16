"""
Erzeuge eine Grafik eines Pacman-Gespensts
"""

from pytamaro.de import (drehe, dreieck, gruen, kreis_sektor,
                         leere_grafik, neben, rechteck, ueber, zeige_grafik,
                         Grafik)

def zeichne_gespenst(hoehe : int, breite : int)  ->Grafik:
    """
    Zeichne eine Grafik eines Pacman- Gespensts in leuchtgruen

    :param hoehe: Gesamthoehe des Gespenstes
    :param breite: Gesamtbreite des Gespenstes
    :returns: die Grafik des Gespenstes
    """
    
    halbkreis_kopf : Grafik = drehe(180,kreis_sektor(breite//2,180,gruen))
    rechteck_bauch : Grafik = rechteck(breite, hoehe -breite/4,gruen)
    einzel_zacke : Grafik = drehe(180,dreieck(breite/6, gruen))
    zeichne_zacken : Grafik = leere_grafik()
    for i in range(3):
        zeichne_zacken = neben(zeichne_zacken,neben(einzel_zacke,einzel_zacke))
    return ueber(halbkreis_kopf,ueber(rechteck_bauch,zeichne_zacken))

zeige_grafik(zeichne_gespenst(200,400))


