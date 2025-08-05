#data structures

#inbuilt data structures(list,dictionary,tuple sets)
#user_defined data structrures(stack,tree,queue,linkedList, graph, hashmap)

#Lists and Tuples:

list_a=["Today",1,"Monday","Busy"]
list_a.insert(len(list_a),"Now")
print(list_a)
list_b=[1,2,3,4,5,4,4,6]
print(f"Index 0 is {list_b[0]}")
print(f"Index 1 is {list_b[1]}")
print(f"Index 2 is {list_b[2]}")
print(f"Index 3 is {list_b[3]}")
list_b.insert(len(list_b),7)
list_b.append(8)
list_b.extend(["32",86,"James"])
print(list_b)
print(list_b.count(2))
pop_item=list_b.pop(list_b[0])
print(pop_item)
print(list_b.count(2))
 
 #to loop in list
for idx,item in enumerate(list_b,1):

    print(idx," ",item)

list_c=["Being","Ledger","Green","Borrow"]
list_d=["Green","Brown",["Gender","age"],"Down","Leep"]
list_e=["23",2,3.0,"John"]

#empty list
number=[]
number.extend(["Martin","Karim","lebo","cleo","Dan"])

print(number)

#printing specifc range of items
print(number[1:4])

#print index from specifc index to last
print(number[3:])

#printing items from index 1 all through
print(number[:])

#printing items at index 2
print(number[-3])

new_num=list_b.count(2)-list_b.count(4)
print(new_num)

#list cpmression
numbers=[n*n for n in range(1,16)]
print(f"THese are the numbers in power of 2 from 1 to 16 {numbers}")

#-------SETS-------
#stores uniqe items no duplicate

students_id={233,343,454,543,676,455}
print(students_id)

#initiating empty set
empty_set=set()
print(empty_set)
empty_set.add(44)
print(f"updated set is: {empty_set}")


#---union of sets
a={"James","Karim","Letoo"}
b={"James","LUCAS","Martin"}
print(f"the union of a and b is {a.union(b)}")

#---------diff of sets------
print(f"Difference of a and b is: {a.difference(b)}")

#-----intersection
print(f"Intsersection of a and b is: {a.intersection(b)}")

#---comparison----

if a==b:
    print(f"Set {a} is equal to set {b}")
else:
    print(f"set {a} is not equal to set {b}")

#adding dta to set
company={"Finance","ICT","BOARD","Customer"}
updated_data=["KRA","SECURITY","VENDORS"]
company.update(updated_data)
print(company)

#deleting dta from a set
company.discard("KRA")
print(company)

#adding total value of numbers in a set
numbers={2,4,6,7}
print(sum(numbers))

 #looping in set
for idx, x in enumerate(numbers,1):
    print(f"{idx}: {x}") 

"""x=6
while x>=6:
    print(f"length: {len(numbers)} and the number is {x**3}" )   
"""
##printing duplicate set
duplicate_set={3,3,4,1,3,4,7,8,9,5,7}
print(duplicate_set)

#initializing empty dictionary
empty_dict={}
print(empty_dict)

first_data={1 : "James", 2 :"Martin", 3 :"Karim"}
print(first_data)

#----adding element to dictionary---------
capital_city={"Kenya":"Nairobi","Uganda":"Kampala","Nigeria":"Lagos"}
capital_city["South A"]="Johanesburg"
print(capital_city)

#change value to  DICTIONARY----
students_id={111:"Karim",112:"Tom",114:"Jerry"}
del students_id[111]
print(students_id)

#---access element in dictionary
print(students_id[114])

#deleting all dictionary

#new_dta=students_id.clear()
print(students_id)

#--mebership test----
students_id={1:"Mary",2:"Karim",3:"Tom",4:"Jerry"}
print(students_id)

print("Tom" not in students_id)

all={1:1,2:2,3:3,4:4,5:4}
check={4,6,5}
for x in check:
    if(x in all):
     print(f"{x} is in { all} ")
    else:
        print(f"{x} is not in {all}")
