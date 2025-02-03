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
