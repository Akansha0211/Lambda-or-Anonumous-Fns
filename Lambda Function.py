#BASIC USE OF LAMBDA FUNCTION
# def add(x,y):
#     return x+y
# print(add(2,3))
# def minus(x,y):
#     return x-y
# print(minus(9,3))

# minus=lambda x,y:x-y
# print(minus(9,4))

# def cube(n):
#     return n*n*n
# a=lambda x:x*x*x
# number=int(input("Enterr sn integer"))
# print("using lambda:",a(number))
# print("using function:",cube(number))

# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# final_list=[]
# for i in list:
#     if i%2==0:
#         final_list.append(i)
# print("Final list",final_list)

#OR
#USING LAMBDA Fn ALONG WITH FILTER
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# final_list = list(filter(lambda x: (x%2 == 0),lst))
# print(final_list)

# li=[1,2,3,4,5,6,7,8,9,10,11]
# final_list=list(map(lambda x:x*2,li))
# print(final_list)

# from functools import reduce
# list=[1,2,3,4,5,6,7,8,9,10,11]
# final_list=reduce((lambda x,y:x+y),list)
# print(final_list)

#This is a part of functools  module.

