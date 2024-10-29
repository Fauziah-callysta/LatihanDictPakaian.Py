import os
import random
import string
data = dict()
while True:
    os.system("cls") # WIN
    # os.system("clear") # mac/linux
    print(f" {'DATA PAKAIAN':❤^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    jenis = input("Masukkan Jenis Pakaian\t:")
    ukuran = input("Masukkan Ukuran Pakaian\t:")
    warna = input("Masukkan Warna Pakaian\t:")
    data[keyFinal] = {
        keyFinal: {
            'jeniskey': jenis,
            'ukurankey': ukuran,
            'warnakey': warna
        }
    }
    
    opsi = input("Input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-" * 40)
print(f"Key\t Jenis\t Ukuran\t Warna")
print("-" * 40)
for key, value in data.items():
    print(f"{key}.\t {data[key][key]['jeniskey']}\t {data[key][key]['ukurankey']}\t {data[key][key]['warnakey']}")