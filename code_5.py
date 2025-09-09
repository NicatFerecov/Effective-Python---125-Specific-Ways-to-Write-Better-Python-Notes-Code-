a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Middle two:  ", a[1:5])
print("All but ends:", a[1:7])

print(a[:5] == a[0:5]) # True donecek
print(a[:5] == a[1:5]) # False donecek

assert a[5:] == a[5:len(a)]
print(a[5:] == a[5:len(a)])

a[:]      # ["a", "b", "c", "d", "e", "f", "g", "h"]
a[:5]     # ["a", "b", "c", "d", "e"]
a[:-1]    # ["a", "b", "c", "d", "e", "f", "g"]
a[4:]     #                     ["e", "f", "g", "h"]
a[-3:]    #                          ["f", "g", "h"]
a[2:5]    #           ["c", "d", "e"]
a[2:-1]   #           ["c", "d", "e", "f", "g"]
a[-3:-1]  #                          ["f", "g"]

first_twenty_items = a[:20]
last_twenty_items = a[-20:]
# print(last_twenty_items)
# print(first_twenty_items)


# aynı eksik dizine doğrudan erişmek bir istisna oluşturur:
try:
	a[20] # IndexError: list index out of range
except IndexError:
	print("Xeta.")
finally:
	print("eksik dizine doğrudan erişmek bir istisna oluşturur.")


b = a[3:]
print("Before:   ", b)
b[1] = 99
print("After:    ", b)
print("No change:", a)

print()


# print(a[2:7])
print("Before ", a)
a[2:7] = [99, 22, 14]
print("After  ", a)

print()

print("Before ", a)
a[2:3] = [47, 11]
print("After  ", a)

b = a
print("Before a", a)
print("Before b", b)
a[:] = [101, 102, 103]
print(a is b)             # Still the same list object
assert a is b
print("After a ", a)      # Now has different contents
print("After b ", b)      # Same list, so same contents as a