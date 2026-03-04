# def list_lenth(lis_t):
#     print(len(lis_t))


# def list_element(lis_t):
#     #for ele in lis_t:
#     print(lis_t)


# lis=["apple","mango","guava"]
# list_lenth(lis)
# list_element(lis)

def factorial(n):
    fac=1
    for el in range(1,n+1):
        fac*=el
    print("factorial:",fac)

n=int(input("enter number:"))
factorial(n)