
myList = [(2, 5), (9, 4), (9, 0), (1, 4), (1, 5)]
print("Initially the list is : " + str(myList))

# joining tuples if similar initial element
joinList = []
for val in myList:										
	if joinList and joinList[-1][0] == val[0]:			
		joinList[-1].extend(val[1:])						
	else:
		joinList.append([ele for ele in val])	
joinList = list(map(tuple, joinList))

# Printing the joined List
print("Joined list : " + str(joinList))
