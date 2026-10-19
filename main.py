def nand(x, y):
    return not (x and y)

def f_awal(a, b, c, d):
    return (c or d) and (a or (b and c and d))

def f_sederhana(a, b, c, d):
    return (a and c) or (a and d) or (b and c and d)

def f_nand(a, b, c, d):
    term1 = nand(a, c)          
    term2 = nand(a, d)

    bc_not = nand(b, c)
    bc = nand(bc_not, bc_not)
    bcd_nand = nand(bc, d)

    temp = nand(term1, term2)
    temp_not = nand(temp, temp)
    hasil_akhir = nand(temp_not, bcd_nand)
    
    return hasil_akhir
semua_cocok = True
for i in range(16):
    a, b, c, d = (i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1
    x = bool(f_awal(a, b, c, d))
    y = bool(f_sederhana(a, b, c, d))
    z = bool(f_nand(a, b, c, d))
    cocok = (x == y == z)
    semua_cocok = semua_cocok and cocok
    print(a, b, c, d, "|", int(x), int(y), int(z), "|", "OK" if cocok else "BEDA")
print("Semua 16 kombinasi cocok:", semua_cocok)
