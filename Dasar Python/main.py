nama = "Faris"

print(nama)

jumlah = 0
for i in range(1, 11):
  jumlah += i

print(jumlah)

if nama == "Faris":
  print("Nama adalah Faris")
else:
  print("Nama bukan Faris")

def sapa(nama):
  print(f"Halo, {nama}!")

sapa("Faris")
