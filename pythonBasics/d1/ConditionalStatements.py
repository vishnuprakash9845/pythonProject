# conditional if else

age=int(input("Enter the person age"))

if age>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

num = age

if num%2==0:
    print("Given number is even")
else:
    print("Given number is odd")

num1=11

print("Given number is even") if num1%2==0 else print("Given number is odd")

{print("hello"),print("python")} if num1>=15 else {print("Bye"),print("python")}


weekno=10

if weekno==1:
    print("sunday")
elif weekno==2:
    print("monday")
else:
    print("Invalid week")

