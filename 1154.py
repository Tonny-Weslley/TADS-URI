tot = []
while True:
    num = int(input())
    if(num >= 0):
        tot.append(num)
    else:
        soma = 0
        for numero in tot:
            soma += numero
        print('{:.2f}'.format(soma/len(tot)))
        break