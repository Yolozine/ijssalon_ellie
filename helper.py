def decoreer(tekst=""):
    lengte = len (tekst) + 4 
    print ()
    print (lengte * "*") 
    print (f"* {tekst} *") 
    print (lengte * "*") 
    print () 

def fooi_pp (bedrag , personen) : 
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep (tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst)*"=")
    return uit

def som(inkomsten):
    return sum(inkomsten.values())

inkomsten = {
    "aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

resultaat = som(inkomsten)
print("De totale som van de inkomsten is:", resultaat)