import random


#1
adatok = []
darabszam = 100
for db in range(darabszam):
    adatok.append(random.randint(50,150))
print(adatok)


#összegség tétele
#sun - határoza meg az adatok lista elemek összegét
sum = 0
for item in adatok:
    sum += item

print(f"sum(list) - {sum}")

#átlag - az adatok részletének meghatározása

sum = 0
for item in adatok:
    sum += item
atlag = sum / len(adatok)

print(f"atlag(list) - {atlag}")

#prod- az elemek szorzatának meghatározása
prod = 1
for item in adatok:
    prod *= item
atlag = sum / len(adatok)

print(f"prod(list) - {prod}")

#min-max tétel
#min -határoza meg adatok legkisebb elemét

min = adatok[0]
for item in adatok:
    if item < min:
        min = item

print(f"min(list) - {min}")


#max - határoza meg a legnagyobb számot

max = adatok[0]
for item in adatok:
    if item > max:
        max = item

print(f"max(list) - {max}")

#megszámlálás tétele
# határoza meg a 120nál nagyobb elemek db számát

db1 = 0
for item in adatok:
    if item > 120:
        db1 += 1

print(f"db1(list) - {db1}")

#határoza meg a 100jegyel kezdödö elemeket


db2 = 0
for item in adatok:
    if item == 100:
        db2 += 1

print(f"db2(list) - {db2}")

#eldöntés tétele
#legalább egy elem teljesíti a feltételt
#döntse el hogy az elemek között van e 50-es értékű elem

vanE_50 = False
for item in adatok:
    if item == 50:
        vanE_50 = True
        break

if vanE_50:
    print("A lista tartalmaz legalább 1 olyan elemet amely értéke 50")
else:
     print("A lista nem tartalmaz 50-es értékű elemet")    

#minden elem teljesíti
#döntse el hogy az adatok lista minden eleme kissebb mint 150

mindenE_kissebb150 = True
for item in adatok:
    if not (item) < 150:
        mindenE_kissebb150 = False
        break

if mindenE_kissebb150:
    print("A lista összes eleme kissebb mint 150")
else:
     print("A lista nem összes eleme kissebb mint 150")   

#kiválasztás tétele
#!!!!!!!!!!!!! előfordul hogy amit szeretnénk kiválasztani olyan nincs is
#határozza meg a lista 50-es értékű elemnének első elemének leőfordulását

elem50 = None
for item in adatok:
    if item == 50:
        elem50 = item
        break
if elem50 != None:
    print(f"van megfelelő elem amely értéke: {elem50}")
else:
    print("nincs ilyen elem")   

#keresés tétele
#!!!!!!!!! ha nincs megfelelő elem akkor nincs megfelelő indexe
# határozza meg az adatok listábana 100-as értékü elem helyét(előfordulásának helyét)

index100 = None
for i in range(len(adatok)):
    if adatok[i] == 100:
        index100 = i
        break

if index100 !=  None:
    print(f"van megfelelő elem (100-as értékű), amely értéke: {index100}")
else:
    print("nincs ilyen elem")   
           

#buborékos rendezés
#rendezzük az adatok listát növekvő sorrendbe
for i in range(len(adatok)-1, 0, -1):
    for j in range(i):
        if adatok[j] > adatok[j+1]:
            adatok[j], adatok[j+1] =  adatok[j+1], adatok[j]

print(adatok)







