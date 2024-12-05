prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5,
}
aanbieding = prijzen["aardbei"] * 0.8
# reclame_tekst = "Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts €"

reclame_tekst = f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts €{aanbieding}"

# Deze suggestie kreeg ik van chatGPT, vele malen eenvoudiger te begrijpen dan index en TypeError enzo??
reclame_tekst2 = f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts €{aanbieding:.2f}"

# hoofdletters
reclame_tekst3 = (reclame_tekst2.upper())

# split naar list
reclame_tekst4 = (reclame_tekst3.split())

# onder mekaar
for el in reclame_tekst4:
  if len(el) >= 5: 
        print(el.upper())  
  else:
        print(el.lower())

