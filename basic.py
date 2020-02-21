import sys
import traceback

"""
- Python is dynamically strongly typed
- Once the data type of a variable is determined by the code it cannot be changed later.
- Python dynamic typing could be a problem. Dynamic typing can produce dynamin errors and that can be avoided in two ways.
Solution to that is using type hinting, where you can annotate
a function but still it cannot stop the erronous code from running.
Another solution to that is writing unit tests but that could also be an issue when it comes to larger code bases
"""

#- String formats
str1 = "String_value_one"
str2 = "String_value_two"
str3 = "String_value_three"

# formatted string where the variable can be substituted with {}
print(f"This is a string {str1}\n")

# raw string
print(r"This is a raw string 12 12 2 12 12. Everything will be printed as it is including this var {str1}\n", "\n")

#string formatter with sequence of number of variables
#the sequence starts from zero if nothing is passed then default zero is used
print("The string is {1} and then it is also {0} but not this {2}\n".format(str1, str2, str3))
print("This string {} and this {}".format(str1, str3, str2)) # the last argument is ignored

#Boolean, True or false values. Unlike in Java it's in title case
b = True
print("Bool value is {0}".format(b))

# None value. Like in other languages have Null in C# and null in Java. Python has None
# All it means is var is defined but no value is assigned yet. Later it can be assigned some value to it. Any value.
# This is more of an advance declaration but does not save us from dynamic typing errors

none_var = None
print("Var type before is {type(none_var)}" )
none_var = 1
print(f"Var-> value {none_var}. Var->type {type(none_var)}")
# Notice how the type was determined later

# if checks on the None value
if (none_var == None):
    print("The var is None")
else:
    print("The var is NOT None")

# if defined checks
if(none_var):
    print("None_var is defined")
else:
    print("It's not defined")


# ternary operator OR single line if statement
a = 1
b = 2
print("A is greater") if (a > b) else print ("B is greater")

################## List and list functions #############################################
# Lists - Arrays in other languages but heteroginous data types are allowed
lst = [ "A", "AAA", "BBB", 4 ]
print(lst)

#checking if an element is in the list
print("In") if ("A" in lst) else print("Out")
#Here ("A" in lst) returns True

#number of elements in List with len function. len(lst)
print(len(lst))

# element in the list with index, last element with -1, Indices are circular
print(lst[1]) # second element
print(lst[-1]) # last element

# other operators
#append
lst.append("YY")
print(lst)

#pop - pops top element
print(lst.pop())
print(lst)

#remove - remove the given value
lst.remove("A")
print(lst)

# ?? more practice

#list splicing - slicing the list with range. This range excludes the last element e.g. if the range is from 0-9 this will not include the 9th element which is "ten" in this case.
astr = "One two three four five six seven eight nine ten".split()
print(astr)
print(astr[0:9]) # print 8 elements
print(astr[1:-1]) # everything except first and last element
print(astr[9:1]) # will not print anything since the range is not valid but program will compile

############################ end of list functions ###################################


########################### loops ####################################################
# for loops

# ! Range function produces range. It takes, start, end and stepping argument
for i in range(0,5):
    print(f"Ele -> {i}")

for i in range(0,10,2):
    print("Ele2 -> {0}".format(i))

# if, else, elif
if(1>2):
    print(1)
elif(2>1):
    print(2)
else:
    print(None)

# Loop breakers break / continue
for i in (range(1,100)):
    print(i)
    if (not (i % 2)):
        print(f"Found even{i}. Quiting")
        break
    else:
        print(f"Did not find even {i}, Continuing")
        continue

# While loops. There is no += , -=. There are no ++ and --
# there is not do while loop in python
x = 1
while( x < 4 ):
    print('X')
    x+=1
############################# end of loops ###################################################

############################# dictionaries ###################################################

# python dictionary is a perl hash, defined with curly braces but access with square brackets and heterogenous data types are allowed
hsh = { "a": 1, "b": 2, "c": 3, 1: 99 }

#keys for all keys
for i in hsh.keys():
    print(f"K {i} ::: V {hsh[i]}")

# with items
for k,v in hsh.items():
    print(f"Key {k} Val {v}")

# with enumerate
for k,v in enumerate(hsh):
    print(f"K-{k} => V-{v}")

# get only values
for v in hsh.values():
    print(f"Vals {v}")

#printing full hash
print(hsh)

#printing single element in the hashs
print(hsh["a"])

#deleting a key
del hsh["a"]
print(hsh)

# adding new element to hashs, While adding you can use [] again. But for initial declaration only use {};
hsh["X"] = 9
print(hsh)

# if key does not exist then python will throw an exception called KeyError

######################################### end of dictionaries #########################################


######################################### Tuples #########################################

# tuples are const arrays defined with (), accessed with [] and heterogenous data types are allowed, immutable
tup = (1, 2, 33, 33, "A", 'X')
print(tup)

# access length of tuple
print("Count is", len(tup))

#access one element with []
print("One element", tup[1])

# tup[4] = 3 : This fails because tuples does not support assignments

for i in (range(0,len(tup))):
    print(f"{i} -> {tup[i]}")

##########################################################################################


############################## Sets ################################
#sets are arrays but unique, defined with curly braces and accessed with square braces and have heterogenous elements
# sets are also immutable and will not support object assignment
set1 = { 1, 2, '#', 4}
print(set1)

# set count
print(len(set1))

# set1[1] = 'Z' # this fails 
# print(set1)

#access one element # looks like accessing one element from a set is not possible without iterating through it
# print(set1[1]) will fail

############## end of sets ############################################

