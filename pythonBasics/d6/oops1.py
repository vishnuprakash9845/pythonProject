
# class MyClass:
#
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print(name)
#
# mc1=MyClass()
# mc2=MyClass()
#
# mc1.myfun()
# mc2.display("vishnu")

# class MyClass:
#     def m1(self):
#         print("this is instance method")
#
#     @staticmethod
#     def m2(self,num):
#         print(num)
#
# mc = MyClass()
# mc.m1()
# mc.m2(100,200)

# class MyClass:
#     a,b=10,20
#     def add(self):
#         print(self.a+self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
# m1=MyClass()
# m1.add()
# m1.mul()

# i,j=15,25 # global variables
#
# class MyClass:
#     a,b=10,20 # class variables
#
#     def add(self,x,y): #x,y are local variables
#         print("Local varaibles",x+y)
#         print("Class varaibles", self.a + self.b)
#         print("Global varaibles", i + j)
#
# m1 = MyClass()
#
# m1.add(2,3)

# Constructor eg

class MyClass:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("hello....")

    def m2(self,x,y):
        return(x+y)

m1=MyClass() # invoke constructor automtically
m1.m1() # call explicitly
res=m1.m2(10,20)
print(res)
