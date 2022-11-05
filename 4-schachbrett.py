"""
Erzeuge eine Grafik eines Schachbretts
"""

from pytamaro.de import rechteck, schwarz, leere_grafik, rgb_farbe, ueber, neben, zeige_grafik

BRETT_GROESSE = 400
GROESSE = BRETT_GROESSE // 8
SCHWARZ = schwarz
WEISS = rgb_farbe(255, 200, 120)

brett = leere_grafik()
