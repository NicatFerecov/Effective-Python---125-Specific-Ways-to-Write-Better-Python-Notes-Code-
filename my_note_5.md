# Know How to Slice Sequences

Date: 9.09.2025

The basic form of the slicing syntax is `somelist [start:end]`; here, the start is included, but the end is excluded:
*Note: start is included, end is excluded.*

When slicing to the end of an array, you should omit the final index as it is unnecessary.

*Note:*
Indexing a list with a negative variable is one of several situations where you may get surprising results from the slicing operation. For example, the expression somelist[-n:] works correctly when n is greater than zero (e.g., somelist[-3:] when n is 3). However, when n is zero, the expression somelist[-0:] is equivalent to somelist[] and creates a copy of the original list.

The result of slicing a list is an entirely new list. Each element in the new list references the corresponding objects in the original list. Modifying the list created by slicing does not affect the contents of the original list.

If you omit the start and end indices when slicing, you will obtain a copy of the entire original list.


## Things to Remember
1. Avoid excessive detail when slicing: Do not specify 0 for the start index or the length of the array for the end index.
2. Slicing accepts start or end indices outside the bounds, which means it is easy to express slices at the front or back of an array (e.g., a[:20] or a[-20:]).
3. Assigning to a list slice replaces the referenced range in the original array, even if the lengths differ.