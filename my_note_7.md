# Prefer Catch-All Unpacking over Slicing

Date: 9.09.2025


	oldest, second_oldest, *others = car_ages_descending
	print(oldest, second_oldest, others)
This code is shorter, easier to read, and eliminates the error-prone fragility of boundary indices that must be synchronised across lines.
A starred expression can appear in any position (beginning, middle, or end), so you can always take advantage of the catch-all unpacking when you need to extract an optional slice.
However, when using a starred expression in an extraction assignment, you must have at least one mandatory part; otherwise, you will get a syntax error. You cannot use the all-encompassing expression on its own.
# Example:
	*others = car_ages_descending
	>>>
	Traceback ...
	SyntaxError: starred assignment target must be in a list or tuple
*Note*: You cannot use multiple general expressions in a single opening pattern.
Starred expressions always become list comprehensions. If there are no remaining elements in the unpacked sequence, the encompassing part will be an empty list.
However, because a starred expression is always converted to a list, unpacking an iterator carries the risk of consuming all your computer's memory and causing your programme to crash. Therefore, you should only use the all-encompassing unpacking operation on iterators when you have good reason to believe that all the result data will fit in memory.

## Key Points to Remember
1. Unpacking assignments may contain a starred expression to store all values not assigned to other parts of the unpacking pattern in a list.
2. Asterisked expressions can appear anywhere in the unpacking pattern. They always result in a list containing zero or more values.
3. When splitting a list into non-overlapping parts, the all-encompassing unpacking operation is far less prone to errors than using separate expressions for slicing and indexing.