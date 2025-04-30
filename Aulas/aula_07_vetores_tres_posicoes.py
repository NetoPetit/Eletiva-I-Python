v1 = []
v2 = []
s = []

for i in range(3):
    v1.append(int(input("V1[%d]: " %i)))

for i in range(3):
    v2.append(int(input("V2[%d]: " %i)))

for i in range(3):
    s.append(v1[i] + v2[i])

print(s)