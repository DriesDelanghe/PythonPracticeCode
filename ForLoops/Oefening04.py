getallen = list()

i = 0
while i < 5:
    try: 
        getal = int(input("geef een getal: "))
        getallen.append(getal)
    except BaseException:   
        if(i == 0):
            i = 0
        else:
            i = i-1
    i = i+1

sumNr = 0
for i in range(5):
        sumNr += getallen[i]

average = sumNr/5

print(getallen, "gemiddelde: ", average)
