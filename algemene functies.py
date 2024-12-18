#Huiswerkopgave 2
def mijn_functie_1(zichzelf):
    return zichzelf * zichzelf

print (mijn_functie_1(12))

#Huiswerkopgave 3
def mijn_functie2(num1, num2):
    totaal = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 
    }
    return totaal

resultaten = mijn_functie2(12, 3)
print(resultaten['+'])  
print(resultaten['-'])  
print(resultaten['*'])  
print(resultaten['/']) 

#voor de overige argumenten 12,2, 10,5, 100,20 kan je de parameters in de functie aanpassen

