
getal = int(input("geef een aantal: "))


prevfib = 0
fib = 1

print(prevfib)
print(fib)
for i in range(getal - 2):
    fib = prevfib + fib
    print(fib)
    prevfib = fib
