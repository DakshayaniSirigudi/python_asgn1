##########python   lists########
#create a list

list1=[1,'name',34.6]
print(list1)
print(type(list1))   #gives the datatype of the list
print(list1[0])     #accessing of list items
print(list1[1])
print(list1[2])
list2=['apple',1.2,56,'apple',1234,34.8]    #duplicates are allowed
print(list2)
print(len(list2))     #length of a list1
print(list1[-1])    #negative indexing----prints from the last
print(list2[2:4])   #shows from index2 upto index4 but excluding index4
print(list[:3])     #shows from beginning element to index 3 but excluding it
print(list[2:])     #shows from index 2 to last element
if 1.2 in list2:    #checking the presence of the element in a list
   print("1.2 is in this list")
list2[1:3]=[27,'fruit']    #changing elements
print(list2)
list2[2:3]=['cake',196]    #assigning multiple values oin the place of previous single elements
print(list2)
list1.insert(1,'nuts')      #inserting at the given index
print(list1)
list1.append(78)         #add at the append
list1.extend(list2)      #append elements from list2 to list1
print(list1)
list1.remove('apple')    #removing specified elements
print(list1)
list1.pop(4)             #removing element based on index2
print(list1)
del list1[7]
print(list1)
list2.clear()      #clears the element but list is still present
print(list2)
########list  loops#######
##for loop##

for x in list1:      #prints the list elements by using iteration
   print(x)

for i in range(len(list1)):    #gives the indices of the list
      print(i)

##while  loop##

i=0
while i<len(list1):
  print(list1[i])
  i=i+1


#############python   dictionaries##########
dict1={
"fruit":"banana",
"snack":"cake",
"year":1947
}
print(dict1)
print(dict1["snack"])    #accessing the dictionary elements
x=dict1.get("fruit")     #other way of accessing elements
print(x)
print(len(dict1))        #length of the dictionary
dict1={
"fruit":"banana",
"snack":"cake",
"year":1947,
"snack":"bun"
}                    #     duplicates are not allowed in the dictionary,
                    #     here cake is replaced with bun
print(dict1)
print(len(dict1))
print(type(dict1))
y=dict1.keys()        #shows the keys of the dictionary
print(y)
z=dict1.values()      #returns the values of the dictionary
print(z)
x=dict1.items()    #returns each item in a dictionary
print(x)
dict1["year"]=1987    #changing the value of an item
print(x)
dict1.update({"fruit":"apple"} )   #another method of changing the value
print(dict1)
if "fruit" in dict1:     #check if key is present
    print("yes,fruit is one of the keys of this dictionary")
dict1["colour"]="red"     #adding new item using index
print(dict1)
dict1.update({"age":"25"})    #adding item using arguments
print(dict1)
dict1.pop("year")      #removes the item with specified key
print(dict1)
dict1.popitem()     #removes the last item
print(dict1)
del dict1["colour"]    #deletes the specified key
print(dict1)
dict1.clear()       #clears the complete dictionary which means no item is present in the dictionary but empty dictionary remains
print(dict1)
del dict1         #deleting the entire dictionary which means there is no dictionary left
print(dict1)
                 #creting new dictionary
dict2={
"name":"leo",
"age":27,
"height":6.1,
"weight":76,
"colour":"white"
}
#print(dict2)
##########loops in dictionary##########
##for loop##
for x in dict2:       #gives the keys of the dictionary
    print(x)
for x in dict2.keys():   #another method for printing keys
    print(x)
for x in dict2:              #gives the values of the items in the dictionary
    print(dict2[x])
for x in dict2.values():     #another methiod for printing the values
    print(x)

for x,y in dict2.items():
    print(x,y)

######copying dictionary######

dict3=dict2.copy()     #copying using copy()
print(dict3)

dict4=dict(dict2)      #copying using dict()
print(dict4)

###nested dictinary###
diction={
"dict2":dict2,
"dict3":dict3
}
print(diction)
