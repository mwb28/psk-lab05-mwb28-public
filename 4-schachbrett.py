"""
Erzeuge eine Grafik eines Schachbretts
"""

from pytamaro.de import rechteck, schwarz, leere_grafik, rgb_farbe, ueber, neben, zeige_grafik, Grafik, Farbe





def zeichne_schachbrett(groesse : int,)-> Grafik:
    """
    Zeichne ein Schachtbrett mit hellbraunen und schwarzen Feldern
    :param groesse: die Grösse des Schachbretts in Pixel
    :returns: das Schachbrett als Grafik
    """
    weiss : Farbe = rgb_farbe(255, 200, 120)
    rechteck_braun : Grafik = rechteck(groesse/8,groesse/8,weiss)
    rechteck_schwarz : Grafik = rechteck(groesse/8,groesse/8,schwarz)
    linie1 : Grafik = leere_grafik()
    linie2 : Grafik = leere_grafik()
    brett : Grafik = leere_grafik()
    for i in range(4):
        linie1 = neben(linie1, neben(rechteck_braun,rechteck_schwarz))
        linie2 =neben(linie2, neben(rechteck_schwarz,rechteck_braun))
    for i in range(4):
        brett= ueber(brett, ueber(linie1,linie2))
    return brett

zeige_grafik(zeichne_schachbrett(200))

