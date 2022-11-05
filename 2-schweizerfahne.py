"""
Erzeuge eine Grafik der Schweizerfahne und zeige diese an.
"""

from pytamaro.de import rechteck, rot, weiss, drehe, ueberlagere, zeige_grafik

# schreib hier Deine Lösung von Aufgabe 2

SEITE = 320
grund = rechteck(SEITE, SEITE, rot)
horizontal_arm = rechteck(SEITE // 32 * 20, SEITE // 32 * 6, weiss)
vertikal_arm = rechteck(SEITE//32*6,SEITE //32*20,weiss)
zeige_grafik(ueberlagere(ueberlagere (drehe(90,horizontal_arm),horizontal_arm),grund))
