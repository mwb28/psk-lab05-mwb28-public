"""
Erzeuge eine Grafik eines Pacman-Gespensts
"""

from pytamaro.de import zeige_grafik, dreieck, drehe, kreis_sektor, rechteck, neben, ueber, gruen, leere_grafik

BREITE = 400
HOEHE = 200
DREIECK= drehe(180,dreieck(BREITE//6,gruen))
RECHTECK= rechteck(BREITE,HOEHE,gruen)
HALBKREIS= drehe(180,kreis_sektor(BREITE//2,180,gruen))
zeichne_zacken = leere_grafik()
for i in range(3):
    zeichne_zacken= neben(zeichne_zacken,neben(DREIECK,DREIECK))

zeige_grafik(ueber(HALBKREIS,ueber(RECHTECK,zeichne_zacken)))


