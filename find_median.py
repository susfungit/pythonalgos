def findMedianSortedArrays(nums1:list[int],nums2:list[int]) -> float:
	len1=len(nums1)
	len2=len(nums2)
		
	i=0
	j=0
	resultlist=[]
	while i < len1 and j < len2:
		if nums1[i] < nums2[j]:
			resultlist.append(nums1[i])
			i+=1
		else:
			resultlist.append(nums2[j])
			j+=1
	resultlist=resultlist + nums1[i:] + nums2[j:]
	middle=len(resultlist)//2
	return  (resultlist[middle] + resultlist[~middle])/2

