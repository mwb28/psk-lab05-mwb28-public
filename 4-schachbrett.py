"""
Erzeuge eine Grafik eines Schachbretts
"""

from pytamaro.de import rechteck, schwarz, leere_grafik, rgb_farbe, ueber, neben, zeige_grafik

BRETT_GROESSE = 400
GROESSE = BRETT_GROESSE // 8
SCHWARZ = schwarz
WEISS = rgb_farbe(255, 200, 120)
brett = leere_grafik()
rechteck_braun = rechteck(GROESSE,GROESSE,WEISS)
rechteck_schwarz = rechteck(GROESSE,GROESSE,SCHWARZ)

zwei_splatenA= neben(rechteck_braun,rechteck_schwarz)
vier_spaltenA = neben(zwei_splatenA,zwei_splatenA)
acht_spaltenA = neben(vier_spaltenA,vier_spaltenA)

zwei_spaltenB= neben(rechteck_schwarz,rechteck_braun)
zwei_spaltenB = neben(zwei_spaltenB,zwei_spaltenB)
acht_spaltenB = neben(zwei_spaltenB,zwei_spaltenB)

zwei_zeilen= ueber(acht_spaltenA,acht_spaltenB)
vier_spalten = ueber(zwei_zeilen,zwei_zeilen)


zeige_grafik(ueber(vier_spalten,vier_spalten))



