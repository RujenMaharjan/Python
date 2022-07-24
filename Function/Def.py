# def nepal():
#     print("Nepal")
#
# nepal()

# def name(firstname, secondname):
#     print(firstname, secondname)
#
# name("Rujen","Maharjan")



# def name():
#     return [10,10,10]
# def calc():
#     a=name()
#     p=a[0]
#     t=a[1]
#     r=a[2]
#     return (p*t*r)/100
# def disp():
#     print(calc())
#
# disp()




# def val(arg):
#     def tup(a,b):
#         if a==0 or b==0:
#             return "One of the value is 0"
#         else:
#             return arg(a,b)
#     return tup
# @val
# def add(x,y):
#     return x+y
#
#
# print(add(1,2))
#


# def decorator_list(fnc):
#     def inner(list_of_tuples):
#         return [fnc(val[0], val[1]) for val in list_of_tuples]
#     return inner
#
#
# @decorator_list
# def add_together(a, b):
#     return a + b
#
#
# print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))



# def pow(x,y):
#     return math.pow(x,y)
#
# print(pow(2,3))

#
# import datetime
# def dat():
#     return datetime.datetime.now()
#
# print(dat())

# import math
# print(math.sin(60))

# from datetime import day
# x= date.today()
#
#
# print(f"Today is {x}")