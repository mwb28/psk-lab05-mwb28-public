"""
Erzeuge eine Sequenz von Grafiken eines Pacmans,
mit unterschiedlich weit geöffnetem Mund.
Speichere die Sequenz als animiertes GIF.
"""

from pytamaro.de import (Grafik, Farbe, drehe, fixiere, gelb, kombiniere,
                         kreis_sektor, rechteck, schwarz, speichere_gif,
                         ueberlagere, zeige_grafik, rgb_color)

PACMANCOLOR  : Farbe= rgb_color(255,255,0)
BACKGROUNDCOLOR : Farbe = schwarz
BACKGROUNDSQUARE : Grafik = rechteck(400,400,BACKGROUNDCOLOR)
LIST_PACMAN : list = []

def erzeuge_pacman_frames(groesse: int, winkel_min: int, winkel_max: int, schritt: int) -> list[Grafik]:
  winkel_mindef : int = 360 - winkel_min 
  winkel_maxdef : int = 360 - winkel_max
  winkel_schritt : float  = (winkel_maxdef- winkel_mindef)/(schritt-1)
  list_pacman : list = []
  for i in range (schritt):
    winkel_pacman :float = winkel_mindef + (winkel_schritt * i)
    ausrichtung_pacman : float = winkel_pacman/2 +180
    list_pacman.append( kombiniere(fixiere("links", "mitte",drehe(ausrichtung_pacman,kreis_sektor(groesse,winkel_pacman,PACMANCOLOR))),BACKGROUNDSQUARE))
  return list_pacman

LIST_PACMAN = erzeuge_pacman_frames(100,15,180,20)



speichere_gif("animated_pacman", LIST_PACMAN, 30, True)



