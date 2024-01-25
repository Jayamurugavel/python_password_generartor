a=[]
sum=0
for i in range(5):
    b=int(input("enter numer="+str(i+1)))
    #print(b)
    a.append(b)
print(a)

for i in a:
    sum=sum+i
    avg=sum//5
print(sum)
print(avg)