belanja = [
    {"Buah":"Semangka","Harga":12000},
    {"Buah":"pepaya","Harga":10000},
    {"BUah":"Nanas","Harga":12000},
]

total_belanjaan = 0
for item in belanja:
    total_belanjaan+= item["Harga"]

print("Total belanja:", total_belanjaan)    