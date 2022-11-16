"""
Erzeuge eine Grafik der deutschen Flagge und zeige diese an.
"""

from pytamaro.de import rechteck, rgb_farbe, ueber, zeige_grafik, Grafik

# komplettiere hier Deine Lösung von Aufgabe 1
BREITE : int= 500
HOEHE : int= BREITE * 3 // 5
FARBEN : list = [rgb_farbe(0, 0, 0), rgb_farbe(255, 0, 0), rgb_farbe(255, 204, 00)]

def zeichne_deutsche_flagge()-> Grafik:
    """
    Erzeugt eine deutsche Flagge mit der Breite 500 px.
    @returns: die deutsche Flagge als Grafik
    """
    schwarzes_rechteck = rechteck(BREITE, HOEHE // 3, FARBEN[0])    
    rotes_rechteck = rechteck (BREITE, HOEHE//3, FARBEN[1] )    
    goldenes_rechteck = rechteck (BREITE, HOEHE//3, FARBEN[2] )

    return ueber(schwarzes_rechteck, ueber(rotes_rechteck,goldenes_rechteck))


zeige_grafik(zeichne_deutsche_flagge()) 
