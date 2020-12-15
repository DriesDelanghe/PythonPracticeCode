
getal = int(input("geef een getal: "))

for i in range(getal):
    multi = getal * (i+1)
    print(str(getal), "*", str(i + 1), "=", str(multi))