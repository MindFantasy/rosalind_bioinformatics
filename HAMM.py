with open("rosalind_hamm.txt", "r") as file:
    sequence = file.readlines()

sequence = str(sequence)
separator = sequence.find(",")
string_1 = sequence[2:separator - 3]
string_2 = sequence[separator + 3:-4]


length = len(string_1)
h_d = 0 # hamming distance

for i in range(length):
    if string_1[i] != string_2[i]:
        h_d += 1

print(h_d)