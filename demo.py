aj=('a','b','c')
jk=('e','f')
aj+=jk
print(aj)


aj *=2
print(aj)
print(aj[5])
print(aj[1:5])

mylist=["aws",250000]
mylist1=["spark",500000]
mylist+=mylist1
print(mylist)

mylist.append("1500000")
print(mylist)

mylist3=["Machine Learning",5000000]
mylist.append(mylist3)
print(mylist)

mylist.insert(1,"Cloud")
print(mylist)