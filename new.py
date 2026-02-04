# *
def my_asc(*numbers):
    num=[*numbers]
    # a=num[0]
    # order=[]
    i=len(num)
    # print(i)
    # print(num[1])
    # for b in range(1,i):
    #     # print(b)
    #     # print(a)
    #     # print(num[b])
    #     if a>num[b]:
    #         a=a
    #     else:
    #         a=num[b]
    # order.append(a)
    # for gh in num:
    #     if a>gh:
    #         a=a
    #     else:
    #         a=gh
    # order.append(a)
            
    # print(order)
            

    for b in range(i):
        for c in range(b+1,i):
            if num[b]>num[c]:
                num[b],num[c]=num[c],num[b]
                       
    
    print(num)
my_asc(5,8,3,9)