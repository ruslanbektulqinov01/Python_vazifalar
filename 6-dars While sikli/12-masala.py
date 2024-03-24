n = int(input("n sonini kiriting (1 dan katta butun son): "))

k = 1
yigindi = 0

while yigindi + k <= n:
    yigindi += k
    k += 1

print(f"Eng katta k: {k - 1}")
print(f"Yig'indining qiymati: {yigindi}")
