# s="welcome"
# s='welcome'
# s=str("welcome")
# s=str('welcome')
#
# print(s)

name=""
name=''
name=str()

#mutable - can change value of the variable
#immutable - cannot change value of the variable

#stings are immutable

# str1="welcome"
# print(str1)
# print(id(str1)) #4513419056
#
# str1 = str1 + "to python"
# print(str1)
# print(id(str1)) #4512272256

# str = "welcome"
# print(str+"programming")
# print(str*2)

#slicing
#start index 0
#ending index 1

# w e l c o m e
# 0 1 2 3 4 5 6
#

# str="welcome"

# print(str[1:3])  # e l
# print(str[:6])   # w e l c o m
# print(str[2:])   # l c o m e
# print(str[1:-1]) # e l c o m
#
# print(ord('A'))
# print(ord('a'))
#
# print(chr(65))
# print(chr(98))
#
# print(max(str))
# print(min(str))
# print(len(str))

# print("come1" in str)
# print("come" in str)


#Method-1
s="welcome"

rev_str=""

for i in s:
    rev_str=i+rev_str

print(rev_str)

#Method-2

print(s[::-1])


