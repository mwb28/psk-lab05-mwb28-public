"""
Erzeuge eine Grafik eines Schachbretts mit Text zum Bezeichnen
der waagrechten Reihen (mit Zahlen von 1 bis 8)
und der senkrechten Linien (mit Buchstaben von a bis h).
"""

from pytamaro.de import rechteck, text, schwarz, leere_grafik, rgb_farbe, ueber, neben, zeige_grafik

BRETT_GROESSE = 400
GROESSE = BRETT_GROESSE // 8
SCHWARZ = schwarz
WEISS = rgb_farbe(255, 200, 120)

brett = leere_grafik()
