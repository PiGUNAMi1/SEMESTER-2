



print("\nLOOPING IN PYTHON")
print("--------------------\n")
a = 0
b = float(input("Masukkan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    a += 1 # increment

print("\nPenggunaan Break pada Looping")
print("------------------------\n")
a = 0
b = float(input("Masukkan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    if a == 15: #Seleksi Kondisi
        break # Break Point
    a += 1 # Increment

print("\nPenggunaan continue pada Looping")
print("------------------------\n")
a = 0
b = float(input("Masukkan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    if a == 15: #Seleksi Kondisi
        continue # Continue Point
    a += 1 # Increment

print("\nPenggunaan if else pada Looping")
print("------------------------\n")
a = 0
b = float(input("Masukkan angka anda : "))
while a < b: # a < b adalah syarat
    if a == (b - 1): #Seleksi Kondisi
        print("PErulangan berhenti")
        break;
    else:
        print("Perulangan ke - ", a)    
        a += 1









        