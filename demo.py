s = "Sony12India567Pvt2ltd"

num=""
res=0
for x in range(1,len(s)):
    val = ""
    if s[x].isnumeric():

        val = val + s[x]
        for y in range(x+1,len(s)):
            if s[y].isnumeric():
                num=num+s[y]
            else:
                break
    print(num)




print(res)

