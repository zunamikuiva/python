Auto = []

choice = None #menu
print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
while choice != "0": #Kunnes valinta on yhtä kuin "0"

    print("""Käytettävissä olevat toiminnot:
1) Anna auton tiedot
2) Tulosta autojen tiedot
0) Lopeta""")
    choice = input("Valintasi: ")
    
    # Ulos
    if choice == "0":
        print("Kiitos ohjelman käytöstä.")
 
 
    # tuotten lisäminen
    elif choice == "2":
        print("Listalta löytyy seuraavat automerkit ja hinnat:")
        
        for entry in Auto:
             name, price = entry
             print(name, price,)
        print()

             
 
    # tuotten lisäminen
    elif choice == "1":
        name = input("Anna auton merkki: ") #Nimi
        price = int(input("Anna auton hinta: "))
        entry = (name, price)
        Auto.append(entry) #lisää rivin loppuun
        #suodatin
        print()
    
    else:
        print("Tuntematon valinta, yritä uudestaan.")
        print()
