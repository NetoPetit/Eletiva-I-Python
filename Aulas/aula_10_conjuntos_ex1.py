vetor = []

for i in range(10):
    vetor.append(int(input("Nro %d:" % i)))
print(vetor)
conj = set(vetor)
print(conj)
qtdd = len(conj)
print("Qtdd nros difs = %d" % qtdd)