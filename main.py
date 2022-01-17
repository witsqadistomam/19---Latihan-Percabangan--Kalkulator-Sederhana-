# Latihan

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=","\n")

a = float(input("Masukkan angka a = "))
operator = input("Operator bilangan (+,-,x,/) : ")
b = float(input("Masukkan angka b = "))

if operator == "+":
    hasil = a + b
    print(f"Hasil dari {a} + {b} = {hasil}")
elif operator == "-":
    hasil = a - b
    print(f"Hasil dari {a} - {b} = {hasil}")
elif operator == "*" or operator == "x":
    hasil = a * b
    print(f"Hasil dari {a} x {b} = {hasil}")
elif operator == "/" or operator == ":":
    hasil = a / b
    print(f"Hasil dari {a} / {b} = {hasil}")
else:
    print("Maaf Kami Tidak Dapat Melakukan Operasi Bilangan Tersebut")

print("\n=========SELESAI=========\n")