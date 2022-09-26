def quick_sort(mylist:list):
	list_length=len(mylist)
	if list_length <= 1:
		return mylist
	else:
		pivot_number=mylist.pop()

	left_list=[]
	right_list=[]

	for no in mylist:
		if no < pivot_number:
			left_list.append(no)
		else:
			right_list.append(no)

	return quick_sort(left_list) +  [pivot_number]+quick_sort(right_list)


if __name__ == "__main__":
	print(quick_sort([600,0,33,2,33,91,-2,4,6,34,5,33]))
