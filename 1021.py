saque = float(input())
primeiro = saque

cem = int(saque/100)
saque -= cem*100

cinquenta = int(saque/50)
saque -= cinquenta*50

vinte = int(saque/20)
saque -= vinte*20

dez = int(saque/10)
saque -= dez*10

cinco = int(saque/5)
saque -= cinco * 5

dois = int(saque/2)
saque -= dois * 2

um = int(saque)
saque -= um
saque *= 100


centavos50 = int(saque/50)
saque -= centavos50*50

centavos25 = int(saque/25)
saque -= centavos25*25

centavos10 = int(saque/10)
saque -= centavos10*10

centavos05 = int(saque/5)
saque -= centavos05*5

centavos01 = int(saque)



print('NOTAS:')
print(cem,'nota(s) de R$ 100.00')
print(cinquenta,'nota(s) de R$ 50.00')
print(vinte,'nota(s) de R$ 20.00')
print(dez,'nota(s) de R$ 10.00')
print(cinco,'nota(s) de R$ 5.00')
print(dois,'nota(s) de R$ 2.00')
print('MOEDAS:')
print(um,'moeda(s) de R$ 1.00')
print(centavos50,'moeda(s) de R$ 0.50')
print(centavos25,'moeda(s) de R$ 0.25')
print(centavos10,'moeda(s) de R$ 0.10')
print(centavos05,'moeda(s) de R$ 0.05')
print(centavos01,'moeda(s) de R$ 0.01')