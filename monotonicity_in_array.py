	# Check the monotonicity of a numeric array for all type of  posibilities:
	# A problem which looks seasy if you do sorting but it is T=(nlong), for newbiews
	# I solve this in T=O(N) and Space O(1)
	# Thinking a concept of memory momentum from the Machine Learning gradient search.
	# Unittests are in unittests_monotonic_array.py
	
def isMonotonic(array):
	memoryOfDownDirection = False
	memoryOfUpDirection = False
	NoChangeInDirection = True
	
	if len(array)==0 or len(array)==1 :
		return True
		
	for i in range (1, len(array)):
		# elements are equal for move to the next position of the array and keep the status intact.
		if array[i-1] == array[i]:
			NoChangeInDirection = True
			continue
		# we go downwards
		if array[i-1] > array[i]:
			# if there is memory of previous direction going UP given that now the current state is for  going DOWN
			if memoryOfUpDirection == False:
				memoryOfDownDirection = True
				NoChangeInDirection = True	
			else: 	
				NoChangeInDirection = False	

		# we go upwards	
		if array[i-1] < array[i]:
			if memoryOfDownDirection == False:
				memoryOfUpDirection = True
				NoChangeInDirection = True
			# if there is memory of previous direction going Down given that now the outer if checked for UP
			else:	
				NoChangeInDirection = False
		# if happened a turn from Down to Up or Up to Down 
		if NoChangeInDirection == False:
			break

	return NoChangeInDirection
