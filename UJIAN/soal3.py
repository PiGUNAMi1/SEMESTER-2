# Dictionary dengan nilai-nilai siswa
nilai_siswa = {
    "Siswa 1": 85,
    "Siswa 2": 90,
    "Siswa 3": 78,
    "Siswa 4": 92,
    "Siswa 5": 88
}

# Menghitung jumlah total nilai siswa
total_nilai = 0
for nilai in nilai_siswa.values():
    total_nilai += nilai

print("Jumlah total nilai semua siswa adalah:", total_nilai)