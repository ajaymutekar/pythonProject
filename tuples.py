
#creating a tuple
'''a=(1,2,5)
print(a[0])
'''

# creating tuple using count function
'''a=(2,5,6,4,5,2,6,5,68)
print(a.count(5))
'''
# creating tuple using index function
'''
a=(5,6,7,6)
print(a.index(7))
'''

# student list
'''SSC=input("Enter a name")
HSC=input("Enter a name")
BA=input("Enter a name")
BCOM=input("Enter a name")
BCA=input("Enter a name")
BCS=input("Enter a name")
MCOM=input("Enter a name")
MCA=input("Enter a name")

total=[SSC,HSC,BA,BCOM,BCA,BCS,MCOM,MCA]
print(total)'''


'''a=(15,63,89)
# print(a[1]+a[2])
print(sum(a))
'''

'''a=(7,0,8,0,0,9)
print(a.count(0))'''

a={"city":"Aurangabad",
   "State":"Maharashtra",
   "Country":"India",
   "Aurangabad":{'Taluka':'Khultabad'}
   }
# print(a['Aurangabad']['Taluka'])

print(a.get('Aurangabad'))
print(a)

a=[1,2,3,4]
b=[5,6,7]
c=(a[0]+[1])+(b[0]+[1])
print(sum(c))
