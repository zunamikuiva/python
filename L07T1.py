lista=[]

while (True):
     print("Ostoslistasi sisältää seuraavat tuotteet:")
     print(lista)
     print("""Voit valita alla olevista toiminnoista:
1) Lisää
2) Poista
0) Lopeta""")
     valinta=int(input("Valintasi: "))
     if valinta == 1 :
            Tuote=input("Anna lisättävä tuote: ")
            
            lista.append(Tuote)
            print()
            continue
      
     if valinta == 2 :
            
            
            if not lista:
                  print("Tuote lista on tyhjä")
                  continue
            else:
                 
                 TM = len(lista)
                 print("Ostoslistassasi on " + str(TM) + " tuotetta.")
                 l=int(input("Anna poistettavan tuotteen järjestysnumero: "))
                 print()
                 p=l-1
                 del lista[p]
            continue
     if valinta == 0 :
            if not lista:
                   print("Sinulta jäi ostamatta seuraavat tuotteet:")
                   print(str(lista))
                   print("Kiitos ohjelman käytöstä.")

            else:
                  print("Sinulta jäi ostamatta seuraavat tuotteet:")
                  print(str(lista))
                  print("Kiitos ohjelman käytöstä.")
            break
     else:
          print("Tunnistamaton valinta.")
          print()

        
