# Cek apakah sebuah bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Cetak semua bilangan prima dari 1 hingga 100
print("Bilangan prima antara 1 dan 100:")
for i in range(2, 101):
    if is_prime(i):
        print(i)