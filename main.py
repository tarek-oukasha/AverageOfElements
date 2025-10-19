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
for i in range(len(varlist)-1,-1,-1):
    print(varlist[i])
#or
for i in varlist[::-1]:
    print(i)
#or
for i in reversed(varlist):
    print(i)


animal_list = ['lion','tiger','cheetah','horse','kangaroo','ant','butterfly','beetle','crocodile','alligator','donkey','mouse','cat','dog','fish']

for i in range(len(animal_list)):
    print(animal_list[i])

#how to check if a certain animal is in the list
for animal in animal_list:
    #if we dont use range then "animal"will hold whatever the item is. (see line 74)
    if animal == 'ant' :
        print("ant is in the list")
    else :
        print("")
#or
for i in range(len(animal_list)):
        #if we do use range then "i" will hold the index number. (see line 75)

    if animal_list[i] == 'ant' :
        print("ant is in the list")
    else :
        print("")

print (animal)
print (i)

print()

prices_list = [15,8,25,42,69.99,86,99]

#find the average of the list
average=((sum(prices_list))/7)
print(round(average,2))