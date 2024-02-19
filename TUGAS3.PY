data_penjualan = [
     {"produk":"baju","jumlah":20},
     {"produk":"celana","jumlah":15},
     {"produk":"tas","jumlah":10},
     {"produk":"sepatu","jumlah":25},
]

total_penjualan = 0
for data in data_penjualan:
    total_penjualan += data ["jumlah"]

print("Total penjualan semua produk:", total_penjualan)  