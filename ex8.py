import random
list = []
list1 = []
list2 = []
x=0 

'''Getting in the list random numbers'''
for t in range(0,30):
	list.insert(t , random.choice([-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
print "Random Numbers list : \n" , list

'''Putting in list2 the triads with sum 0'''
for i in range(0,29):
	for j in range(0,29):
		for k in range(0,29):
			if (list[i] + list[j] +list[k] == 0):
				list1.insert(x,[list[i],list[k],list[j]])	
				x+=1

'''Sorting the triads'''
for a in list1:
	if sorted(a) not in list2:
		list2.append(sorted(a)) 


'''Print the triads'''
print "The different triads with sum 0 are :"
for b in list2:
	print b,"\n"