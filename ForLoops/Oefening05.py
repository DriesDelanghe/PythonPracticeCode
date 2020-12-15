getallen = list()

i = 0
while i < 10:
    try: 
        getal = int(input("geef een getal: "))
        getallen.append(getal)
    except BaseException:   
        if(i == 0):
            i = 0
        else:
            i = i-1
    i = i+1

kleinsteGetal = getallen[0]
grootsteGetal = getallen[0]

for i in range(10):
    if(getallen[i] < kleinsteGetal):
        kleinsteGetal = getallen[i]
    if(getallen[i] > grootsteGetal):
        grootsteGetal = getallen[i]

print("grootste getal: ", grootsteGetal, "kleinste Getal: ", kleinsteGetal)

