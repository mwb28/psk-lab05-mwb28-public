"""
Erzeuge eine Grafik eines Pacmans
"""

from pytamaro.de import kreis_sektor, gelb, drehe, zeige_grafik, Grafik

def zeichne_pacman(groesse : int, mundwinkel : int,) -> Grafik:
    """
    Zeichne eine Grafik eines gelben Pacman, der gegen rechts ausgerichtet ist
    :param groesse: groesse des pacmans in Pixel
    :param mundwinkel: Öffnung des Pacmanmundes in Grad
    :returns: die Grafik des Pacmans
    """
    mundwinkel_effektiv : int = 360- mundwinkel
    return drehe(mundwinkel_effektiv/2 +180,(kreis_sektor(groesse, mundwinkel_effektiv, gelb)))


zeige_grafik(zeichne_pacman(100,15))

