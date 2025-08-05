#data structures

#inbuilt data structures(list,dictionary,tuple sets)
#user_defined data structrures(stack,tree,queue,linkedList, graph, hashmap)

#Lists and Tuples:

list_a=["Today",1,"Monday","Busy"]
list_a.insert(len(list_a),"Now")
print(list_a)
list_b=[1,2,3,4,5,6]
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

