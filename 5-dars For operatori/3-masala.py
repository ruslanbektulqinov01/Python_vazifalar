#a va b butun sonlar berilgan(a<b). a va b sonlari orasidagi sonlarni kamayish tartibida
#chiqarilsin(a va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.

a = int(input("1-sonni kiriting:"))
b = int(input("2-sonni kiriting:"))

for son in range(b, a-1 , -1):
     print(son)

print(f"Sonlar miqdori: {b-a+1}")