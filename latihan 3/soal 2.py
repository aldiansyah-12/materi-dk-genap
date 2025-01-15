#program promosi toko

print("porgram bonus toko")

nilai=int(input("masukan nilai pembelian : "))

if nilai >= 1500000 and nilai<=5000000:
    print("Anda mendapatkan baju Bloodz")
elif nilai >= 500000:
    print("Anda mendapatkan raket")
else:
    print("Anda tidak mendapatkan bonus")