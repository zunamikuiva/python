
import re
nimi1=input("Anna luettavan tiedoston nimi: ")
file = open(nimi1,'r')
L1=len(re.findall(r"[\n']+", open(nimi1).read()))
nimi2=input("Anna kirjoitettavan tiedoston nimi: ")
open(nimi2,'w').write('')
def paaohjelma():
    while (True):
        f=file.readline().replace('\n', '')
        if f == "":
            L2=len(re.findall(r"[\n']+", open(nimi2).read()))
            print("Luettiin " + str(L1) + " riviä tiedostosta '"+nimi1+"'.")
            print("Kirjoitettiin " + str(L2) + " riviä tiedostoon '" + nimi2 + "'.")
            print("Kiitos ohjelman käytöstä.")
            break
        
        if any(ch.isdigit() for ch in f):
            pass
            
        
        else:
            open(nimi2,'a').write(f.lower()+'\n')
        
    
    
   
    file.close()
paaohjelma()
