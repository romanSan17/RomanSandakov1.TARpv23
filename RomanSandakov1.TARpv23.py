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
try:
    kokku=randint(10,100)
    print("Kokku:",kokku)
    mitu=int(input("Mitu kommi tahad võtta?"))
    kokku=mitu
    print("Laua peal on",kokku,"kommid")
except :
    print(no)

#4
#dlina=int(input("Mis on dlina?"))
#diametr=dlina*3.14
#print(diametr)

#5
#H=int(input("Mis on H?"))
#M=int(input("Mis on M?"))
#diagonal=**H^2*M^2
#print(diagonal)

#6
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus / aeg
    print("Sinu kiirus oli " + float(kiirus) + " km/h")
except :
    print("Viga andmetüübiga")


#7
#number1=int(input("What number?" ))
#number2=int(input("What number?" ))
#number3=int(input("What number?" ))
#number4=int(input("What number?" ))
#number5=int(input("What number?" ))
#middlenumber = (number1 + number2 + number3 + number4 + number5)/5
#print("keskmise suvalisest:" + str(middlenumber))

#8
#frog ="""
#    @..@
#   (----)
#  ( \__/  )
#^^ "" ^^
#"""
#print(frog)

#9
#A=int(input("onece side:"))
#B=int(input("twice side:"))
#C=int(input("third side:"))
#P=A+B+C
#print("ümbermõõt:" + str(P))

#10
#pizza=int(12.90)
#chay=pizza/100*10
#summa=pizza+chay
#print("You pay:" + str(summa/2) + " friend pay:" + str(summa/2))

#10(2)
