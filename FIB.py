with open("rosalind_fib.txt", "r") as file:
    string = file.readline()


spacja = " "
n = (string[:string.find(spacja)])
k = int(string[string.find(spacja) + 1:])

number = ""
for i in string:
    if i != " ":
        number += i
    else:
        n = int(number)
        number = ""
k = int(number)

prev_adult, adult, infant = 0, 0, 1


for i in range(2, n + 1):
    adult = prev_adult + infant  # dorastanie
    infant = prev_adult * k
    prev_adult = adult


with open("FIB_solution.txt", "w") as solution:
    population = adult + infant
    solution.write(str(population))
