num = int(input())
i = 0
while True:
    if(num != 0):
        i +=1
        entradas = [int(x) for x in input().split()] 
        print('Teste', i)
        match = 0
        for ticket in range(len(entradas)):
            if (ticket+1 == entradas[ticket]):
                match = entradas[ticket]
        print(match)
        print()
    else:
        break   
    num = int(input())