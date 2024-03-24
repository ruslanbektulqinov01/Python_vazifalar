#a va b butun sonlar berilgan(a>b). a va b sonlari orasidagi sonlarni o‘sish tartibida chiqarilsin(a
#va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.


a= int(input("a ni kiriting:"))
b = int(input("b ni kiriting:"))

for son in range (a, b + 1 ):
    print(son)

miqdor= b - a + 1

print(f"Sonlar miqdori: {miqdor} ta")