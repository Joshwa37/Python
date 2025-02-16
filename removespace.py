a="a a "
x=len(a)
count=0
for i in range(1,x+1):
    if(a[-i]!=" "):
        print(a[-i])
        count=count+1
    if(count>=1 and a[-i]==" "):
        print(count)
        break
print(count)
