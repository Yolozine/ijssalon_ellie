#vraag 5
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."

resultaat = aanbieding_1("aardbei", 4, 0.1)
print(resultaat)

#vraag 6
def inkomsten_totaal1(inkomsten):
    totaal = sum(inkomsten)
    return totaal
#voorbeeld van het gebruik van de functie:
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
totaal_inkomsten = inkomsten_totaal1(inkomsten_per_dag)

print("Het totaal van de inkomsten deze week is:", totaal_inkomsten)

#vraag 7
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    totaal_inclusief_btw = totaal * (1 + btw)
    bedrag_btw = totaal * btw
    
    resultaat = f"Het totaal van alle inkomsten van deze week is {totaal_inclusief_btw:.2f} euro, waarover {bedrag_btw:.2f} euro staat,komt de btw."
    return resultaat

# Voorbeeld van het gebruik van de functie
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
resultaat = inkomsten_totaal(inkomsten_per_dag, btw_percentage)

print(resultaat)

#vraag 8
def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

#voorbeeld van het gebruik van de functie
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)

print("Laagste en hoogste inkomsten:", resultaat)

#vraag 9
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = totaal / aantal
    return gemiddelde_waarde

#voorbeeld gebruik van de functie:
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten_per_dag)

print("Het gemiddelde van de inkomsten deze week is:", resultaat)

#vraag 10
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = totaal / aantal
    
    resultaat = f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."
    return resultaat

#voorbeeld van het gebruik van de functie
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten_per_dag)

print(resultaat)

#vraag 11
def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def meervoudig(invoer_lijst):
    if 5 <= len(invoer_lijst) <= 10:
        return laag_en_hoog(invoer_lijst)
    else:
        return "De lijst moet tussen de 5 en 10 integers bevatten."

#voorbeeld van het gebruik van de functie
voorbeeld_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(voorbeeld_lijst)

print("Laagste en hoogste waarde:", resultaat)

#vraag12

def combinatie(invoer_lijst_2):
    return meervoudig(invoer_lijst_2)

# Voorbeeld van het gebruik van de functie
voorbeeld_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = combinatie(voorbeeld_lijst)

def mijn_functie2(korte_lijst):
    return f"De laagste waarde is {korte_lijst[0]} en de hoogste waarde is {korte_lijst[1]}."

#voorbeeld van het gebruik van de functies
voorbeeld_lijst = [10, 5, 3, 2, 1, 2, 9]
korte_lijst = combinatie(voorbeeld_lijst)  
resultaat = mijn_functie2(korte_lijst)      