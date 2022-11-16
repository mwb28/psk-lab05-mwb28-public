"""
Erzeuge eine Grafik der Schweizerfahne und zeige diese an.
"""

from pytamaro.de import rechteck, rot, weiss, drehe, ueberlagere, zeige_grafik, Grafik

# schreib hier Deine Lösung von Aufgabe 2

def zeichne_schweizer_flagge(groesse : int)-> Grafik:
    seite : int = groesse
    grund : int = rechteck(seite, seite, rot)
    horizontal_arm : int = rechteck(seite // 32 * 20, seite // 32 * 6, weiss)
    return ueberlagere(ueberlagere (drehe(90,horizontal_arm),horizontal_arm),grund)


zeige_grafik(zeichne_schweizer_flagge(320))
