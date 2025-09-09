a = "\x07"
print(a)
print(repr(a))

int_value = 5
str_value = "5"

b = eval(repr(a))
assert a == b
print(b)

print("Is %r == %r?" % (int_value, str_value))
print(f"Is {int_value!r} == {str_value!r}?")


class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
    	return f"OpaqueClass({self.x!r}, {self.y!r})"
    # def __str__(self):
    # 	return f"{self.x} and {self.y}"

obj = OpaqueClass(1, "foo")
print(obj)

class StringifiableBetterClass(OpaqueClass):
    def __str__(self):
        return f"({self.x}, {self.y})"
obj2 = StringifiableBetterClass(2, "bar")
print("Human readable:", obj2)
print("Printable:     ", repr(obj2))