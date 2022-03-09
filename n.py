from bs4 import BeautifulSoup
import requests
import json

# toitude veebileht
url = "http://192.168.22.172/menu-example/"

# arvuti küsib mis faili nimi võiks olla
fail = input("Mis võiks faili nimi olla? ")

# teeb ja avab faili
f = open(fail, "x")

# loen lehe sisu
sisu = requests.get(url).text

# tee sellest bs mooduli jaoks arusaadav objekt
doc = BeautifulSoup(sisu, "html.parser")

# otsib kogu infot id järgi
hind1 = doc.find(id="P")
hind2 = doc.find(id="S")
hind3 = doc.find(id="M")
hind4 = doc.find(id="J")

# otsib vajaliku infot
toidud1 = hind1.find_all("li", class_="list-group-item")
toidud2 = hind2.find_all("li", class_="list-group-item")
toidud3 = hind3.find_all("li", class_="list-group-item")
toidud4 = hind4.find_all("li", class_="list-group-item")

# prindib infot ja kirjutab selle faili

for i in range(1):
    f.write("Praad:\n")
    for t in toidud1:
        f.write(t.text)
        f.write("\n")

    f.write("Supid:\n")
    for t in toidud2:
        f.write(t.text)
        f.write("\n")

    f.write("Magustoidud:\n")
    for t in toidud3:
        f.write(t.text)
        f.write("\n")

    f.write("Joogid:\n")
    for t in toidud4:
        f.write(t.text)
        f.write("\n")
        
# paneb faili kinni        
f.close()
            
