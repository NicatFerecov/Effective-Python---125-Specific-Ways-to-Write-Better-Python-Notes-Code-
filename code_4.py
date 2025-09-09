my_test1 = "hello" "world"
my_test2 = "hello" + "world"
assert my_test1 == my_test2
print(my_test1)
print(my_test2)

x= 1
my_test1 = (
    r"first \ part is here with escapes\n, "
    f"string interpolation {x} in here, "
    'this has "double quotes" inside'
)
print(my_test1)

y = 2
my_test2 = r"fir\st" f"{y}" '"third"'
print(my_test2)

my_test3 = r"fir\st", f"{y}" '"third"'
print(my_test3)


my_test4 = [
    "first line\n",
    "second line\n",
    "third line\n",
]
print(my_test4[0] + my_test4[1])


import sys

first_value = ...
second_value = ...

class MyData:
    ...

value2 = MyData(123,
                first_value,
                f"my format string {x}" +  # Explicit
                f"another value {y}",
                "and here is more text",
                second_value,
                stream=sys.stderr)