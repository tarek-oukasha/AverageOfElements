varlist = [1,2,3,'sjdie',4.76,True,{'name':'Tarek'},32,7.81,'hello']


for i in varlist:
    print(i)

#printing each value of the list using the index

print(varlist[0])
print(varlist[1])
print(varlist[2])
print(varlist[3])
print(varlist[4])
print(varlist[5])
print(varlist[6])

print()
print()
print()
print()

for i in range(len(varlist)):
    print(varlist[i])

print()
print()
print()
print()

#code to print the 1st and 2nd items
print(varlist[0:2])


#code to print the 3rd 4th and 5th items
print(varlist[2:5])

#print the last 3 items of the list
print(varlist[7:])
#or
print(varlist[-3:])

#print the list in the reverse order
for i in range(len(varlist)):
    print(varlist[i])
