def bubble_sort(mylist:list):
	list_length=len(mylist)-1
	is_sorted=False
	
	while not is_sorted:
		is_sorted=True
		for i in range(0,list_length):
			if mylist[i+1] < mylist[i]:
				is_sorted=False
				mylist[i],mylist[i+1]=mylist[i+1],mylist[i]

	return mylist


print(bubble_sort([4,2,0,9,4,-1]))
