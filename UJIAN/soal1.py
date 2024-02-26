# Cetak semua bilangan ganjil dan genap dari 1 hingga 100
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")