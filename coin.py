import random

def lempar_koin():
  return random.choice(["Angka", "Gambar"])

lempar = int(input("Masukkan Jumlah Lempar: "))

total_angka = 0
total_gambar = 0

for i in range(lempar):
 
  if (lempar_koin() == "Angka"):
    total_angka += 1 
  else:
    total_gambar += 1


print("Total Angka: " + str(total_angka))
print("Total Gambar: " + str(total_gambar))
print("Persentase Angka: " ,total_angka/lempar)
print("Persentase Gambar: " ,total_gambar/lempar)
