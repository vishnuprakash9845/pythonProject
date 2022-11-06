

# global_var=20 # global variable
#
# def func():
#     local_var=10
#     print(local_var)
#     print(global_var)
#
# func()

# Access global inside function

# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
#
# cool()
# print(x)

# def func(i,j):
#     print(i,j)
#
# #func(10,20)
# func(j=20,i=10)

def my_func(a,b,c):
    print(a,b,c)

#my_func(10,20,30)

my_func(a=10,c=23,b=13)
