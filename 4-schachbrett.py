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

linie1 = leere_grafik()
linie2 = leere_grafik()
brett = leere_grafik()
for i in range(4):
    linie1 = neben(linie1, neben(rechteck_braun,rechteck_schwarz))
    linie2 =neben(linie2, neben(rechteck_schwarz,rechteck_braun))
for i in range(4):
    brett= ueber(brett, ueber(linie1,linie2))

zeige_grafik(brett)

# zwei_spaltenA= neben(rechteck_braun,rechteck_schwarz)
# vier_spaltenA = neben(zwei_spaltenA,zwei_spaltenA)
# acht_spaltenA = neben(vier_spaltenA,vier_spaltenA)

# zwei_spaltenB= neben(rechteck_schwarz,rechteck_braun)
# vier_spaltenB = neben(zwei_spaltenB,zwei_spaltenB)
# acht_spaltenB = neben(vier_spaltenB,vier_spaltenB)

# zwei_zeilen= ueber(acht_spaltenA,acht_spaltenB)
# vier_spalten = ueber(zwei_zeilen,zwei_zeilen)


# zeige_grafik(ueber(vier_spalten,vier_spalten))



