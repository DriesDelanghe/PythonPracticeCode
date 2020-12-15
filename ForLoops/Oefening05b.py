getal = int(input("geef een getal: "))

fac = 1
for i in range(getal):
    fac *= (i+1)

print("De faculteit van ", getal, " is ", fac)