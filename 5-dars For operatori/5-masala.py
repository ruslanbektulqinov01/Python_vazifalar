# 1 kg konfetning narxi berilgan. 0,1, 0,2, …, 1 kg konfetning bahosi chiqarilsin.
narx = float(input("Narxni kiriting:"))
for kg in range(1, 11):
    baho = kg * narx
    print(f"{kg} kg konfetning bahosi: {baho}")