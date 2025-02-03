from presentatie import *
import csv
inkomsten = {
    "aardbeien-ijs-totaal": 1000,
   "Vanille-ijs-totaal": 2000,
  "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}
print(inkomsten)

from helper import *

totaal_inkomsten = som(inkomsten)

print("De totale som van de inkomsten is:", totaal_inkomsten)

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])