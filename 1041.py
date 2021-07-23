a = input().split(" ")
numeros = []
for num in a:
    numeros.append(int(num))
ordem = sorted(numeros)

for num in ordem:
    print(num)
for num in numeros:
    print(num)