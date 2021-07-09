cardapio = [4.00, 4.50, 5.00, 2.00, 1.50]
escolha = input().split(' ')
print('Total: R$ {:.2f}'.format(cardapio[int(escolha[0]) - 1] * int(escolha[1])))