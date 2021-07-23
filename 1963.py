preco = input().split(' ')
dif = float(preco[1])-float(preco[0])
p = (dif * 100)/float(preco[0])
print(f'{p:.2f}%')