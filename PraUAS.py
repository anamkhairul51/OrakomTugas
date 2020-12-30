i = 2748
currentBin = 0       
    
def cetakBin(angka, i):
    a = angka * 2
    b = a / 2
    print('2-------',int(i) % 2)
    print(' ',int(b))

def tukar(i, c):
    temp = i
    i = c
    c = temp
    return c
    
def cetakBinJadi(i, currentBin):
    print('Binner')
    print(" ",i)
    while(i >= 2):   
        current = tukar(i, currentBin)
        i = int(i/2)
        cetakBin(i, current)


cetakBinJadi(i, currentBin)