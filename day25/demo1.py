def testA(a, b):
    print(a)
    print(b)


x='hi'
y='bye'
testA(x,y)

t=('hi','bye')
testA(t[0],t[1])

testA(*t) # automatically takes one element at a time and sends it

# Method overloading not supported
# def testB():
#     print('hi')
#
#
# def testB(a):
#     print(a)
#
#
# def testB(a, b):
#     print(a)
#     print(b)

def testB(*arg):
    print('This is testB')
    print(arg)

testB()
testB('Hi')
testB('Hi','Bye')
