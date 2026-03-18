# find second largest number
number=[12,34,35,64,68,39,88,99,79,35]
maximum=second_largest=float('-inf')
for i in number:
    if i>maximum:
        secomd_largest=maximum
        maximum=i
    elif i>second_largest and i!=maximum:
        second_largest=i
print("second largest value:",second_largest)