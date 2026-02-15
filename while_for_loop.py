# n=int(input("enter number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("sum of ",n," number is:",sum)
 
n=int(input("enter number:"))
fac=1
for el in range(1,n+1):
    fac*=el
print(fac)