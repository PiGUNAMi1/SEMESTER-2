Olahraga = ("Voly", "Senam", "Badminton", 'Lompat', "Basket", "Futsal")
Olahraga_list= list(Olahraga)
print("tuple = ",Olahraga)
print("list = ", Olahraga_list)
Olahraga_list.append("Tenis")
print(Olahraga_list)
del Olahraga_list[3]
print(Olahraga_list)
Olahraga_list[4] = "Sepakbola"
print(Olahraga_list)
Olahraga_tuple = tuple(Olahraga_list)
print(Olahraga_tuple)