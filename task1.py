# leap year or not
'''x =int(input("enter an year"))
if (x%400 == 0) or (x%100!=0 and x%4==0  ):
  print("Leap Year")
else:
  print("Not a Leap Year")'''
# count of vowels in string
'''str1 = input("enter the string : ")
str1_lower = str1.lower()
vowels = "aeiou"
count = 0
for i in str1_lower :
    if i in vowels :
        count = count+1
        print(i,end = " ")
print("\ncount of vowels in given string : ",count)'''

#swap two variables
'''a= int(input("enter the value for a :"))
b= int(input("enter the value for b :"))

temp= a
a=b
b=temp

print("after swapping:")
print("value of a :",a)
print("value of b:",b)'''


# swap value without 3rd variable
'''a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))

a=a+b
b=a-b
a=a-b

print("after swapping :")
print("value of a :",a)
print("value of b :",b)
'''

'''
print(len("Aurangabad"))
print(float(5223))
'''


#functions
'''
def my_function(name):
  print("Good morning",name)

my_function("ajay")
my_function("kiran")
my_function("vikas")

'''

#positional arguments
'''def greet(firstname,lastname):
    print("good morning",firstname,lastname)
    greet("ajay","mutekar")
'''



'''def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
'''


#Arbitary arguments
'''def my_function(*acter):
  print("The popular acter is " + acter[2])

my_function("Akshay", "Ajay", "Rajni")
'''


# keyword arguments

'''def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "chintu", child2 = "sonu", child3 = "golu")
'''

'''ajay="you can use a sub-query in a SELECT INSERT DELETE or  UPDATE statement to perform the following tasks"
ajay=ajay.replace("or","and")
print(ajay)
'''

friends=[10,17,50,15,30]
friends.remove(17)
print(friends)
