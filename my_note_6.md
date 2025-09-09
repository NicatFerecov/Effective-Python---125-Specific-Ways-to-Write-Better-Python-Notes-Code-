# Avoid Striding and Slicing in a Single Expression

Date: 9.09.2025

In addition to the basic slicing operation, Python includes a special syntax for specifying the stride length of a slice in the form of a list **[start:end:stride]**. This allows you to take every nth element when slicing a list. For example, the stride length facilitates grouping based on even and odd row numbers in a list.

*Example:*
	Here, ::2 means **"Select every second element starting from the beginning"**. The more complex ::-2 means **"Select every second element starting from the end and moving backwards"**.
What does *2::2* mean? And what is the difference between *-2::-2, -2:2:-2 and 2:2:-2*?
	*Example:*
	
	x[2::2]     # ["c", "e", "g"]
	
	x[-2::-2]   # ["g", "e", "c", "a"]
	
	x[-2:2:-2]  # ["g", "e"]
	
	x[2:2:-2]   # []

	output:
	>>>
	['c', 'e', 'g']
	['g', 'e', 'c', 'a']
	['g', 'e']
	[]
If you need to use a step, choose a positive value and skip the start and end indices. If you need to use a step with start or end indices, consider using one assignment for stepping and another for slicing.

## Things to Remember
1. Specifying the start, end, and step length together in a single slice can be extremely confusing.
2. If you need to step, try to use only positive step values without start or end indices; avoid negative step values.
3. If you need the start, end, and step length in a single slice, consider making two assignments (one for the step length, the other for slicing) or using islice from the itertools built-in module.