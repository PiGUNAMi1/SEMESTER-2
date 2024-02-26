# Dictionary dengan informasi harga dan jumlah buah
belanjaan = {
    "Apel": {"harga": 5000, "jumlah": 10},
    "Jeruk": {"harga": 3000, "jumlah": 5},
    "Mangga": {"harga": 7000, "jumlah": 7},
    "Pisang": {"harga": 2000, "jumlah": 20},
    "Semangka": {"harga": 15000, "jumlah": 1}
}

# Menghitung total belanjaan Ibu Sari
total_belanja = 0
for buah, info in belanjaan.items():
    total_harga = info["harga"] * info["jumlah"]
    total_belanja += total_harga
    print(f"Total harga {buah}: Rp{total_harga}")

print("Total belanjaan Ibu Sari adalah: Rp", total_belanja)