i = 2748
currentBin = 0   
currentOct = 0
currentHex = 0    

def tukar(i, c):
    temp = i
    i = c
    c = temp
    return c
    
def cetakBin(angka, i):
    a = angka * 2
    b = a / 2
    print('2-------',int(i) % 2)
    print(' ',int(b))
    
def cetakBinJadi(i, currentBin):
    print('Binner')
    print(" ",i)
    while(i >= 2):   
        current = tukar(i, currentBin)
        i = int(i/2)
        cetakBin(i, current)

def cetakOct(angka, i):
    a = angka * 8
    b = a / 8
    print('8-------',int(i) % 8)
    print(' ',int(b))

def cetakOctJadi(i, currentOct):
    print('Octal')
    print(" ",i)
    while(i >= 8):   
        current = tukar(i, currentOct)
        i = int(i/8)
        cetakOct(i, current)

def cetakHex(angka, i):
    a = angka * 16
    b = a / 16
    print('16-------',int(i) % 16)
    print(' ',int(b))

def cetakHexJadi(i, currentHex):
    print('Hexa')
    print(" ",i)
    while(i >= 16):   
        current = tukar(i, currentHex)
        i = int(i/16)
        cetakHex(i, current)

cetakBinJadi(i, currentBin)
cetakOctJadi(i, currentOct)
cetakHexJadi(i, currentHex)