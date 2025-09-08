# a = b"h\x65llo"
# print(type(a))
# x = list(a)
# print(a)
# print(x)
# print("".join((chr(k) for k in x)))



# İlk işlev bir bytes veya str örneği alır ve her zaman bir str döndürür.
def to_str(bytes_or_str) -> str:
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of str

# print(repr(to_str(b"foo")))
# print(repr(to_str("bar")))

# İkinci işlev bir bytes veya str örneği alır ve her zaman bir bytes döndürür:
def to_bytes(bytes_or_str) -> bytes:
    if isinstance(bytes_or_str, str): # eger string tipindedise.
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of bytes

# print(repr(to_bytes(b"foo")))
# print(repr(to_bytes("bar")))

# print(b"one" + b"two")
# print("one" + "two")

# try:
# 	print(b"one" + "two")
# except (TypeError):
# 	print("Byte ile string birleştirilemez.")

# assert b"red" > b"blue"
# assert "red" > "blue"


# blue_bytes = b"blue"
# blue_str = "blue"
# print(b"red %s" % blue_bytes)
# print("red %s" % blue_bytes)
# print("red %s" % blue_bytes)
# print(f"red {blue_bytes}")
# print(b"red %s" % blue_str) # xeta verecek.


# with open("data.bin", "wb") as f: # wb modunda acanda xeta cixmir.
#     f.write(b"\xf1\xf2\xf3\xf4\xf5")