with open("rosalind_gc.txt", "r") as file:
    fasta = file.readlines()

class Content:
    def __init__(self, lable):
        self.lable = lable
        self.string = dict[lable]
        self.content = None

    def counting(self):
        amount = 0
        length = 0
        for line in self.string:
            for letter in line:
                length += 1
                if letter == "C" or letter == "G":
                    amount += 1
        self.content = amount / length * 100

    def info(self):
        self.counting()


dict = {}

for i in fasta:
    if i.find("Rosalind") == True:
        key = i[1::].strip()
        dict.update({key:[]})
    else:
        content = i.strip()
        dict[key].append(content)

lables = []
for key in dict:
    lables.append(Content(key))

for lable in lables:
    lable.info()

result = {}
for key in lables:
    result.update({key.lable:""})
    result[key.lable] = key.content



max_content = max(result.values())
max_lable = max(result, key = result.get)
print(f"{max_lable}\n{max_content:.6f}")



