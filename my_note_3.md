# Understand the Difference Between repr and str when Printing Objects

Date: 9.09.2025

**Repr**:
	When debugging, what you almost always want to see is an object's repr version. The built-in repr function returns a printable representation of an object; this should be the most clearly understandable string serialisation of the object. For many built-in types, the string returned by repr is a valid Python expression.
	Example: *code_3.py*
This is equivalent to using the **%r** format string with the **%** operator or the **!r** type conversion with an **f-string**:


## Key Points to Remember
1. Calling the print function on built-in Python types produces a human-readable value string that hides type information.
2. Calling the repr function on Python's built-in types produces a string containing a printable representation of a value. repr strings can often be passed to the eval built-in function to retrieve the original value.
3. %s format strings produce human-readable strings like str. %r produces printable strings like repr. F-strings produce human-readable strings for substitution text expressions unless you specify the !r conversion suffix.
4. By defining the special __repr__ and __str__ methods in your classes, you can customise the printable and human-readable representation of instances. This can aid debugging and simplify the integration of objects into human interfaces.