import re  # Tuodaan regular expression -kirjasto (re), jolla voi etsiä tekstiä tietyn kaavan mukaan

# Käyttäjä antaa tiedoston nimen, josta luetaan dataa
nimi1 = input("Anna luettavan tiedoston nimi: ")
file = open(nimi1, 'r')  # Avataan tiedosto lukutilassa ('r')

# Lasketaan alkuperäisen tiedoston rivien määrä regexillä (kaikki '\n' -merkit)
L1 = len(re.findall(r"[\n']+", open(nimi1).read()))

# Käyttäjä antaa tiedoston nimen, johon kirjoitetaan suodatettu data
nimi2 = input("Anna kirjoitettavan tiedoston nimi: ")
open(nimi2, 'w').write('')  # Tyhjennetään kirjoitustiedosto ennen kirjoittamista

# Määritellään pääohjelma-funktio
def paaohjelma():
    while True:  # Silmukka, joka jatkaa kunnes tiedosto on luettu loppuun
        # Luetaan rivi kerrallaan, ja poistetaan '\n' -merkit rivin lopusta
        f = file.readline().replace('\n', '')
        
        # Jos rivi on tyhjä, on saavutettu tiedoston loppu
        if f == "":
            # Lasketaan kirjoitustiedoston (nimi2) rivien määrä lopuksi
            L2 = len(re.findall(r"[\n']+", open(nimi2).read()))
            print("Luettiin " + str(L1) + " riviä tiedostosta '" + nimi1 + "'.")
            print("Kirjoitettiin " + str(L2) + " riviä tiedostoon '" + nimi2 + "'.")
            print("Kiitos ohjelman käytöstä.")
            break  # Poistutaan silmukasta ja lopetetaan ohjelma
        
        # Tarkistetaan, sisältääkö rivi numeroita
        if any(ch.isdigit() for ch in f):
            pass  # Jos sisältää, hypätään tämän rivin yli
            
        else:
            # Jos rivi ei sisällä numeroita, se kirjoitetaan kirjoitustiedostoon pienin kirjaimin
            open(nimi2, 'a').write(f.lower() + '\n')
    
    file.close()  # Suljetaan luettava tiedosto lopuksi

# Suoritetaan pääohjelma-funktio
paaohjelma()
