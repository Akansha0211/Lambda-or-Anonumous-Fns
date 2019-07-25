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


#using sorted
def fn(x):
    return x%2
num=[0,1,2,3,4]
a=sorted(num , key = fn)
print(a)

#using sorted with lambda
num=[0,1,2,3,4,5,6,7,8,9]
a=sorted(num, key=lambda x: x%2)
print(a)

#Using filter function along with lambda function
num=[1,2,3,4,5,6,7,8,9]
a=filter(lambda x: True if x%2==0 else False,num)
print(list(a))    #[2, 4, 6, 8]


#Using map with lambda
num=[1,2,3,4,5,6,7,8,9]
a=map(lambda x:x*x,num)
print(list(a))

# def func(x,y,z):
#     return x*y+z
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=int(input("Enter the third number"))
# print(func(a,b,c))

     #OR 
    
# k=int(input("Enter"))
# b=int(input("Enter"))
# c=int(input("Enter"))
# a=(lambda x,y,z:x*y+z)(k,b,c)
# print(a)

    #OR directly
    
a=(lambda x,y,z:x*y+z)(1,2,3)
print(a)


