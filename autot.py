# Alustetaan tyhjä lista autojen tietojen tallentamiseen
Auto = []

# Alustetaan muuttuja valikkoa varten
choice = None
print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")

# Pääohjelman silmukka, joka toistuu, kunnes käyttäjä valitsee lopetuksen (0)
while choice != "0":  # Silmukka jatkuu, kunnes choice on "0"

    # Tulostetaan käyttäjälle valikko ja vaihtoehdot
    print("""Käytettävissä olevat toiminnot:
1) Anna auton tiedot
2) Tulosta autojen tiedot
0) Lopeta""")
    
    # Pyydetään käyttäjältä valinta
    choice = input("Valintasi: ")
    
    # Lopetusvaihtoehto
    if choice == "0":
        print("Kiitos ohjelman käytöstä.")
 
    # Tulostetaan listalla olevien autojen tiedot
    elif choice == "2":
        print("Listalta löytyy seuraavat automerkit ja hinnat:")
        
        # Käydään läpi jokainen auto listassa ja tulostetaan tiedot
        for entry in Auto:
            name, price = entry  # Puretaan nimi ja hinta erikseen
            print(name, price)
        print()  # Tyhjä rivi visuaalista erottelua varten

    # Lisätään auton tiedot listaan
    elif choice == "1":
        name = input("Anna auton merkki: ")  # Pyydetään auton merkki
        price = int(input("Anna auton hinta: "))  # Pyydetään auton hinta
        entry = (name, price)  # Tallennetaan merkki ja hinta tupleen
        Auto.append(entry)  # Lisätään tuple listaan
        print()  # Tyhjä rivi visuaalista erottelua varten
    
    # Jos käyttäjä antaa tuntemattoman valinnan, tulostetaan virheilmoitus
    else:
        print("Tuntematon valinta, yritä uudestaan.")
        print()  # Tyhjä rivi visuaalista erottelua varten
