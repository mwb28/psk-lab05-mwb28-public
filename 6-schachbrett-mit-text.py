"""
Erzeuge eine Grafik eines Schachbretts mit Text zum Bezeichnen
der waagrechten Reihen (mit Zahlen von 1 bis 8)
und der senkrechten Linien (mit Buchstaben von a bis h).
"""

from pytamaro.de import rechteck, text, schwarz,weiss, Farbe, leere_grafik,Grafik, ueberlagere, rgb_farbe, ueber, neben, zeige_grafik, drehe

BRETT_GROESSE = 400
GROESSE = BRETT_GROESSE // 8
SCHWARZ = schwarz
HELL = rgb_farbe(255, 200, 120)
GRUEN = rgb_farbe(51, 153, 51)
WEISS = weiss

FELD_GRUEN = rechteck(GROESSE,GROESSE,GRUEN)
FELD_HELL = rechteck(GROESSE,GROESSE, HELL)
FELD_WEISS = rechteck(GROESSE,GROESSE,WEISS)
SCHRIFTART = "arial"
SCHRIFTGROESSE = 30
SCHRIFTFARBE = SCHWARZ

brett = leere_grafik()

#  text(inhalt: str, schriftart: str, punkte: float, farbe: Farbe) -> Grafik:

def zeichne_Zifferfeld(ziffer : chr) -> Grafik:
    ziffer = text(ziffer,SCHRIFTART,SCHRIFTGROESSE,SCHRIFTFARBE)
    return ueberlagere(ziffer,FELD_WEISS)

def zeichne_Ziffern(startZiffer : str,ausrichtung: str) -> Grafik:
    zeichne_Ziffern_Spalte = leere_grafik()
    unicode_Startziffer = ord(startZiffer)
    for i in range (0,8,2):
        
        if ausrichtung == "unten":
            drehung = 0
            zeichne_feld1 = zeichne_Zifferfeld(chr(unicode_Startziffer+i))
            zeichne_feld2 = zeichne_Zifferfeld(chr(unicode_Startziffer+i+1))
            zeichne_Ziffern_Spalte = neben(zeichne_Ziffern_Spalte,neben(zeichne_feld1,zeichne_feld2))
        elif ausrichtung == "oben":
            drehung = 180
            zeichne_feld1 = zeichne_Zifferfeld(chr(unicode_Startziffer+7-i))
            zeichne_feld2 = zeichne_Zifferfeld(chr(unicode_Startziffer+6-i))
            zeichne_Ziffern_Spalte = neben(zeichne_Ziffern_Spalte,neben(zeichne_feld1,zeichne_feld2))
        elif ausrichtung =="links":
            drehung = 0
            zeichne_feld1 = zeichne_Zifferfeld(chr(unicode_Startziffer+7-i))
            zeichne_feld2 = zeichne_Zifferfeld(chr(unicode_Startziffer+6-i))
            zeichne_Ziffern_Spalte = ueber(zeichne_Ziffern_Spalte,ueber(zeichne_feld1,zeichne_feld2))
        else:
            drehung = 180
            zeichne_feld1 = zeichne_Zifferfeld(chr(unicode_Startziffer+i))
            zeichne_feld2 = zeichne_Zifferfeld(chr(unicode_Startziffer+i+1))
            zeichne_Ziffern_Spalte = ueber(zeichne_Ziffern_Spalte,ueber(zeichne_feld1,zeichne_feld2))

    return drehe(drehung,zeichne_Ziffern_Spalte)


def zeichne_brett()-> Grafik:
    linie1 = leere_grafik()
    linie2 = leere_grafik()
    brett = leere_grafik()
    for i in range(4):
        linie1 = neben(linie1, neben(FELD_GRUEN,FELD_HELL))
        linie2 =neben(linie2, neben(FELD_HELL,FELD_GRUEN))
    for i in range(4):
        brett= ueber(brett, ueber(linie1,linie2))
    return brett

def zeichne_brett_ziffern_links_rechts()-> Grafik:
    return neben(neben(zeichne_Ziffern("1","links"),zeichne_brett()),zeichne_Ziffern("1","rechts"))



zeige_grafik(ueber(ueber(zeichne_Ziffern("A", "oben"),zeichne_brett_ziffern_links_rechts()),zeichne_Ziffern("A", "unten")))













# def zahlen_oben_nach_unten():
#     zahlen_oben_nach_unten= leere_grafik()
#     abstand_rechteck = rechteck(GROESSE,GROESSE,WEISS)

# for i in range (0,8,2):
#     zahl1 = text(str(8-i),"arial",30,SCHWARZ)
#     zahl2 = text(str(8-i-1),"arial",30,SCHWARZ)
#     zahlen_oben_nach_unten= ueber(zahlen_oben_nach_unten,(ueber(zahl1,zahl2)))

# zeige_grafik(zahlen_oben_nach_unten)