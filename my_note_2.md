# Prefer Interpolated F-Strings over C-Style Format Strings and str.format

Date: 8.09.2025

Formatting is the process of combining predefined text with data values to create a single, human-readable message stored as a string. Python has four different string formatting methods built into the language and standard library.

## C-Style Formatting
'%' operators.


The format string uses format specifiers (such as %d) as placeholders that will be replaced with the values on the right-hand side of the formatting expression. The syntax of format specifiers comes from the C language's printf function, which Python (and other programming languages) inherited. Python supports all the usual options you would expect from printf, such as the **%s**, **%x**, and **%f** format specifiers, and supports control over decimal places, padding, filling, and alignment.

There are four issues with C-style format strings in Python. The first issue is that if you change the type or order of the data values in the tuple on the right-hand side of the formatting expression, you may get errors due to type conversion mismatches.

The second problem with C-style formatting expressions is that they become difficult to read when you need to make minor changes to values before formatting them into a string, which is an extremely common requirement.

Another issue with formatting expressions is that if you want to use the same value multiple times in a format string, you must repeat it in the tuple on the right:
	template = "%s loves food. See %s cook."
	name = "Max"
	formatted = template % (name, name)
	print(formatted)

This is particularly tedious and error-prone if you have to repeat small changes in the formatted values. For example, here I call the title() method in one reference but not in the other, which leads to inconsistent output.

The % operator in Python helps solve some of these problems by allowing formatting with a dictionary instead of a tuple. The keys in the dictionary are matched with format specifiers of the same name, such as %(key)s.


Using dictionaries in formatting expressions also increases the level of detail, which is the fourth problem with C-style formatting expressions in Python. Each key must be specified at least twice: once in the format specifier, once as a key in the dictionary, and possibly once more for the variable name containing the dictionary value.

## The format Built-in Function and str.format
You can use this function to format multiple values together by calling the new format method of the str type. Instead of using C-style format specifiers like %d, you can specify placeholders with **{}**. By default, placeholders in the format string are replaced with the corresponding positional arguments passed to the format method, in the order they appear.

One way to think about how this works is that the format specifiers are passed along with the value to the built-in format function (in the example above, format(value, ".2f")). The result of this function call is what replaces the placeholder in the overall formatted string. You can customise the formatting behaviour per class by using the __format__ special method.
Another detail to note with `str.format` is to avoid square brackets ({). You should double them to prevent them from being mistakenly interpreted as placeholders ({{) (just as you need to double the % character to escape it correctly in C-style format strings).

Within curly brackets, you can also specify the positional index of an argument passed to the format method to change the placeholder. This allows you to update the format string to reorder the output without needing to change the right-hand side of the format expression, thus solving the issue mentioned in point 1 above.

The same positional index can be referenced multiple times in the format string without needing to pass the value to the format method multiple times, which solves the third issue mentioned above.

Considering these shortcomings and the problems arising from C-style formatting expressions (the above issues #2 and #4), I generally recommend avoiding the use of the str.format method. It is important to understand the new mini-language used in format specifiers (everything after the colon) and how the built-in format function works. However, the rest of the str.format method should be regarded as a historical artefact that will help you understand how Python's new f-strings work and why they are so great.

## Interpolated Format Strings (F-Strings)
Python 3.6 introduced interpolated format strings (abbreviated as f-strings) to definitively resolve these issues. This new language syntax requires you to prefix the format string with the letter f. This is analogous to prefixing a byte sequence with the letter b and a raw (non-escaped) sequence with the letter r.

All options in the built-in mini-language of the new format can be used after the double colon in the placeholders within the f-string. Furthermore, similar to the str.format method (i.e., with !r and !s), there is also the ability to force values into Unicode and repr strings.
	formatted = f"{key!r:<10} = {value:.2f}"
	print(formatted)
	>>>
	'my_var'   = 1.23

F-strings also allow you to put a complete Python expression inside the placeholder parentheses and solve the above problem #2 by allowing minor changes to be made to the formatted values with a short syntax. Operations that required multiple lines with C-style formatting and the str.format method now fit on a single line.

## Things to Remember
1. C-style format strings using the % operator are prone to various pitfalls and verbosity issues.
2. The str.format method introduces some useful concepts in the mini-language of formatting specifiers, but otherwise replicates the errors of C-style formatting strings and should not be used.
3. F-strings are a new syntax for formatting values into strings and solve the biggest problems of C-style format strings.
4. F-strings are concise yet powerful because they allow arbitrary Python expressions to be placed directly within format specifiers.