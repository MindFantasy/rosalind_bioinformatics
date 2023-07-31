with open ("rosalind_prot.txt", "r") as file:
    string = file.readlines()

sequence = str(string)[2:-4]

translator = {
    "UUU": "F", "UUC": "F", "UUA": "L",
    "UUG": "L", "CUG": "L", "CUU": "L",
    "CUC": "L", "CUA": "L", "AUU": "I",
    "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V",
    "GUG": "V", "UCU": "S", "UCC": "S",
    "UCA": "S", "UCG": "S", "CCU": "P",
    "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T",
    "ACG": "T", "GCU": "A", "GCC": "A",
    "GCA": "A", "GCG": "A", "UAU": "Y",
    "UAC": "Y", "CAU" :"H", "CAC": "H",
    "CAA": "Q", "CAG": "Q", "AAU": "N",
    "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E",
    "GAG": "E", "UGU": "C", "UGC": "C",
    "UGG": "W", "CGU": "R", "CGC": "R",
    "CGA": "R", "CGG": "R", "AGU": "S",
    "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G",
    "GGG": "G", "UAA": "Stop", "UAG": "Stop",
    "UGA": "Stop",
    }


protein_sequence =""
for i in range(0, len(sequence), 3):
    n_triplet = sequence[i:i+3]
    for key in translator:
        if n_triplet == key:
            protein_sequence += translator[key]
print("--------------------------------------")
print(protein_sequence)

