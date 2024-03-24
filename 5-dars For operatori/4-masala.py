#. 1 kg konfetning narxi haqiqiy sonda berilgan. 1,2,…, 10 kg konfetning bahosi chiqarilsin

baho = float(input("Narxni kiriting:"))
for kg in range(1,11):
    jami = kg * baho
    print(jami)