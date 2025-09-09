x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]    # First, third, fifth
evens = x[1::2]  # Second, fourth, sixth
print(odds)
print(evens)

x = b"faust"
y = x[::-1]
print(y)

x = "寿司"
y = x[::-1]
print(y)

try:
	w = "寿司"
	x = w.encode("utf-8")
	y = x[::-1]
	z = y.decode("utf-8")
except UnicodeDecodeError:
	print("Error.")

x = ["a", "b", "c", "d", "e", "f", "g", "h"]
x[::2]   # ["a", "c", "e", "g"]
x[::-2]  # ["h", "f", "d", "b"]

y = x[::2]   # ["a", "c", "e", "g"]
z = y[1:-1]  # ["c", "e"]

# practice
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
x[...]