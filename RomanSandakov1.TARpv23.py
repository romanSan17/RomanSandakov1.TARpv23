#1
#print("Tere maailm!")
#nimi=input("Mis on sinu nimi?") #float()->2.5
#vanus=int (input("Kui vana sa oled?"))
#print("Tere tulemast! "+nimi+". Sa oled "+str(vanus)+" aastat vana")
#print("Tere tulemast!",nimi, ". Sa oled", vanus,"aasta vana")
#print("Tere tulemast! {0} sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja vanus=",vanus,",tüüp on",type(vanus))

#2
#vanus=18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis=True
#print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,",tüüp on",type(eesnimi))
#print("Muutuja pikkus=",pikkus,",tüüp on",type(pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,",tüüp on",type(kas_käib_koolis))

#3
from random import *
kokku=randint(10,100)
print("Kokku:",kokku)
mitu=int(input("Mitu kommi tahad võtta?"))
kokku=mitu
print("Laua peal on",kokku,"kommid")