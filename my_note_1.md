# Know the Differences Between bytes and str

In Python, there are two types that represent sequences of character data: bytes and str. Bytes instances contain raw, unsigned 8-bit values **(usually displayed in ASCII encoding)**


		a = b"h\x65llo"
		print(type(a))
		output:
			<class 'bytes'>

Str instances contain Unicode code points representing text characters in human languages:
	Importantly, a string instance does not have an associated binary encoding, and a bytes instance does not have an associated text encoding. To convert Unicode data to binary data, you must call the encode method of the string. To convert binary data to Unicode data, you must call the decode method of bytes. You can explicitly specify the encoding you want to use for these methods, or you can accept the system default, which is usually UTF-8.

When writing Python programmes, it is important to perform the encoding and decoding of Unicode data at the outermost boundary of your interfaces; this approach is often referred to as the Unicode sandwich. The core of your programme should use the str type, which contains Unicode data, and should not make any assumptions about character encodings. This configuration allows you to be strict about output text encoding (ideally UTF-8) while easily accepting alternative text encodings (such as Latin-1, Shift JIS, and Big5).

The distinction between character data types in Python leads to two common scenarios:
	1. You want to perform operations on raw 8-bit arrays containing UTF-8 encoded strings (or another encoding).
	2. You want to operate on Unicode strings that do not have a specific encoding.


When working with raw 8-bit values and Unicode strings in Python, there are two important considerations.

The first issue is that *bytes* and *str* appear to work in the same way, but their instances are not compatible with each other. Therefore, you must be careful about the types of character sequences you pass.


You can concatenate bytes with bytes and strings with strings:
	print(b"one" + b"two")
	print("one" + "two")
This does not cause an error.

However, if you try to concatenate a byte with a string:
	b"one" + "two"
	output:
		Traceback ...
		TypeError: can't concat str to bytes
Comparing the equality of byte and str instances always returns False, even when they contain exactly the same characters (in this case, the ASCII-encoded "foo"):

## Key points to remember
1. *bytes* contain sequences of 8-bit values, and *str* contains sequences of Unicode code points.
2. Using helper functions, ensure that the inputs you are operating on are the expected character sequence type (8-bit values, UTF-8 encoded strings, Unicode code points, etc.).
3. *bytes* and *str* instances cannot be used with operators (>, ==, +, and %).
4. If you wish to read binary data from a file or write binary data to a file, always open the file in binary mode (e.g., "rb" or "wb").
5. If you wish to read or write Unicode data to a file, pay attention to your system's default text encoding. To avoid surprises, explicitly pass the encoding parameter to the open function.