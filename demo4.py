list = [1,2,4,45,77,89]
max=list[0:7:2]

for x in list:
    if x>max:
        max=x
print(max)