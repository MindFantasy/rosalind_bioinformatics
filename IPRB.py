with open("rosalind_iprb.txt", "r") as file:
    numbers = file.readlines()

numbers = str(numbers).strip()
hom_dom, heterozygous, hom_rec = numbers[2:-4].split()


hom_dom = int(hom_dom)
heterozygous = int(heterozygous)
hom_rec = int(hom_rec)

"""
hom_dom - homozygous dominant
hom_rec - homozygous recesiv
"""
total = hom_dom + hom_rec + heterozygous
#Parents
prop_ddxdd = (hom_dom / total) * ((hom_dom - 1)/ (total - 1))
prop_ddxrr = (hom_dom / total) * (hom_rec/ (total - 1)) + (hom_rec / total) * (hom_dom / (total - 1))
prop_ddxdr = (hom_dom / total) * (heterozygous/ (total - 1)) + (heterozygous / total) * (hom_dom / (total - 1))
prop_rrxrr = (hom_rec / total) * ((hom_rec - 1) / (total - 1))
prop_rrxdr = (hom_rec / total) * (heterozygous / (total - 1)) + (heterozygous / total) * (hom_rec / (total - 1))
prop_drxdr = (heterozygous / total) * ((heterozygous - 1) / (total - 1))

#Children with dominant allele
children_prop_ddxdd = prop_ddxdd * 1
children_prop_ddxrr = prop_ddxrr * 1
children_prop_ddxdr = prop_ddxdr * 1
children_prop_rrxrr = prop_rrxrr * 0
children_prop_rrxdr = prop_rrxdr * 0.5
children_prop_drxdr = prop_drxdr * 0.75

full_propability = children_prop_ddxdd + children_prop_ddxrr + children_prop_ddxdr + children_prop_rrxrr + children_prop_rrxdr + children_prop_drxdr

print(f"{full_propability}")