s=list(map(str,input().split(' ')))
sum1=0
count=0
count1=0
for i in s:
    count1=count1+1
for i in s:
    for j in s:
        if i==j:
            count=count+1
    if count==2:
        sum1=sum1+1
        print("hello")
    count=0
#count1=count1//2
print(count1)
print(sum1)
if sum1==count1:
    print("balanced")
else:
    print("not balanced")

