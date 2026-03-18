# remove dupicate value from list
num=[1,2,3,4,4,4,5,3,6,4,7]
data=[]
for i in num:
    if i not in data:
        data.append(i)
print("Actual list:",num)
print("After removing duplicate:",data)