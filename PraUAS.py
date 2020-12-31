i = int(input("Masukkan bilangan yang akan dikonversi\t:"))


def tukar(i, c):
    temp = i
    i = c
    c = temp
    return c


def convertHex(angka):
    if angka == 10:
        return('= A')
    elif angka == 11:
        return('= B')
    elif angka == 12:
        return('= C')
    elif angka == 13:
        return('= D')
    elif angka == 14:
        return('= E')
    elif angka == 15:
        return('= F')
    else:
        return('')


def cetakBin(angka, i):
    a = angka * 2
    b = a / 2
    print('2-------', int(i) % 2)
    print(' ', int(b))


def cetakBinJadi(i):
    currentBin = 0
    print('Binner')
    print(" ", i)
    while(i >= 2):
        current = tukar(i, currentBin)
        i = int(i/2)
        cetakBin(i, current)


def cetakOct(angka, i):
    a = angka * 8
    b = a / 8
    print('8-------', int(i) % 8)
    print(' ', int(b))


def cetakOctJadi(i):
    currentOct = 0
    print('\nOctal')
    print(" ", i)
    while(i >= 8):
        current = tukar(i, currentOct)
        i = int(i/8)
        cetakOct(i, current)


def cetakHex(angka, i):
    a = angka * 16
    b = a / 16
    c = int(i) % 16
    d = int(b)
    print('16-------', c, convertHex(c))
    print('  ', d, convertHex(d))


def cetakHexJadi(i):
    currentHex = 0
    print('\nHexa')
    print(" ", i)
    while(i >= 16):
        current = tukar(i, currentHex)
        i = int(i/16)
        cetakHex(i, current)


def hasil(angka):
    print('Biner =', bin(angka)[2:], '\t', end=' ')
    print('Octal =', oct(angka)[2:], '\t', end=' ')
    print('Hexa =', hex(angka)[2:], '\t', end=' ')


def cetakSemua(hsl):
    print("--------------------------------------------------")
    cetakBinJadi(hsl)
    cetakOctJadi(hsl)
    cetakHexJadi(hsl)
    print("--------------------------------------------------")
    hasil(i)


cetakSemua(i)
