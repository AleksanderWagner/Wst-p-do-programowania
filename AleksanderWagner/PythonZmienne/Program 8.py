kapital = 1000
oprocentowanie = 1.06
rok = 1
while rok <=3:
    print('Na koncie po', rok, 'okresie kapitalizacji:', kapital*oprocentowanie)
    kapital*=oprocentowanie
    rok+=1
