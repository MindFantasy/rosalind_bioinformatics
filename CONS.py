with open ("rosalind_cons.txt", "r") as file:
    fasta = file.readlines()


dict= {}
# sequences in dict are divided into fragments, there are 16 values under one key
for element in fasta:
    if element.find("Rosalind") == True:
        key = element[1::].strip()
        dict.update({key:[]})
    else:
        content = element.strip()
        dict[key].append(content)

sequence = ""
length = 0
# Whole sequence is under one value
for key in dict:
    for element in dict[key]:
        sequence += element
    dict[key] = sequence
    sequence = ""
    length = len(dict[key])

profile = {"A": [], "C": [], "G":[], "T": [],}
temp_profile = {"A": 0, "C": 0, "G": 0, "T": 0,}
consensus = ""
for i in range (length):
    for key in dict:
        for key2 in temp_profile:
            if dict[key][i] == key2:
                temp_profile[key2] += 1
    consensus += max(profile, key = temp_profile.get)

    for key3 in profile:
        profile[key3].append(temp_profile[key3])
        temp_profile[key3] = 0

with open ("CONS_solution.txt", "w") as solution:
    solution.write(consensus)
    solution.write("\n")
    for key in profile:
        text = key + ": "
        solution.write(text)
        for n_number in profile[key]:
            text = str(n_number) + " "
            solution.write(str(text))
        solution.write("\n")
print("done")