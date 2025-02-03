def presenteer(inkomsten_dict, totaal):
    for item, bedrag in inkomsten_dict.items():
        print(f"{item} : {bedrag} euro")
    
    print("=" * 25)
    
    print(f"totaal : {totaal} euro")