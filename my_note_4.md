# Prefer Explicit String Concatenation over Implicit, Especially in Lists

Date: 9.09.2025


When the + operator is present, the automatic formatter may still change the line break, but at least the author's original intent is clear.
	Example:
		my_test6 = [
	    "first line\n",
	    "second line\n" + "third line\n",
	]

My recommendation is to always use explicit string concatenation when a function call takes multiple positional arguments to avoid any confusion. As in the print example above, if there is only one positional argument, using implicit string concatenation is appropriate. Keyword arguments can be passed using explicit or implicit concatenation, which maximises clarity, because they cannot be misinterpreted as positional arguments after the `=` character.

## Key Takeaways
1. In Python code, when two string literals appear next to each other, they are concatenated as if there were a **+** operator between them, similar to the implicit string concatenation feature in the C programming language.
2. Avoid implicit concatenation of elements in list and tuple literals, as this creates uncertainty about the original author's intent. Instead, you should use explicit concatenation with the + operator.
3. In function calls, it is appropriate to use implicit string concatenation with one positional argument and any number of keyword arguments, but you should use explicit concatenation when there are multiple positional arguments.