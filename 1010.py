peca1 = input().split(" ")
peca2 = input().split(" ")

#array com 0=codigo 1=quantidade 2=valor

valor = (float(peca1[2])*int(peca1[1])) + (float(peca2[2])*int(peca2[1]))

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))