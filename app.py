# hitung luas segitiga sederhana
def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)
    
luas_segitiga()

# Hitung luas lingkaran
def luas_lingkaran():
    r = int(input("Masukkan jari-jari: "))
    luas = 3.14 * r**2
    print("Luas lingkaran adalah: ", luas)

luas_lingkaran()