"""
Erzeuge eine Grafik eines Pacmans
"""

from pytamaro.de import kreis_sektor, gelb, drehe, zeige_grafik


zeige_grafik(drehe(315,(kreis_sektor(200, 270, gelb))))

