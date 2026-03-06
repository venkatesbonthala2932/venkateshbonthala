lst_1 = list(map(int, input("enter the first set to sort : ").split(',')))
lst_2 = list(map(int, input("enter the second set to sort : ").split(',')))

merged = []
i = 0
j = 0

while i < len(lst_1) and j < len(lst_2):
    if lst_1[i] < lst_2[j]:
        merged.append(lst_1[i])
        i += 1
    else:
        merged.append(lst_2[j])
        j += 1

# add leftover elements
merged.extend(lst_1[i:])
merged.extend(lst_2[j:])

print(merged)