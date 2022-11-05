"""
Erzeuge eine Grafik der deutschen Flagge und zeige diese an.
"""

from pytamaro.de import rechteck, rgb_farbe, ueber, zeige_grafik

# komplettiere hier Deine Lösung von Aufgabe 1
BREITE = 500
HOEHE = BREITE * 3 // 5
FARBEN = [rgb_farbe(0, 0, 0), rgb_farbe(255, 0, 0), rgb_farbe(255, 204, 00)]

schwarzes_rechteck = rechteck(BREITE, HOEHE // 3, FARBEN[0])
zeige_grafik(schwarzes_rechteck)
