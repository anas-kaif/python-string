# def cal_sum(n):
    
#     if(n==0):
#         return 0
#     sum=n+cal_sum(n-1)
#     return sum

# print(cal_sum(10))
def element_of_list(lis,idx):
    
    if(idx==0):
        return
    element_of_list(lis,idx-1)
    print(lis[idx-1])
    return
lis=["apple","mango","orange"]
element_of_list(lis,len(lis))