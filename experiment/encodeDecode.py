"""
encode() and decode()

This confused me at first in terms of the terminology.

str.encode() -- return bytes class
bytestring.decode() -- returns a string 

REFS
====

http://stackoverflow.com/questions/15791173/python-strings-and-binary-data

"""

str = "Some String"
bStr = b"byte String"

encStr = str.encode()
print(type(encStr))
print(encStr)

decStr = bStr.decode()  # you decode from bytes to some encoding
print(type(decStr))
print(decStr)

# This next one is explicit about what encoding algorithm to use
decStr = bStr.decode(encoding='utf-8') 
print(type(decStr))
print(decStr)

# This next one performs a complete cycle.
# NOTE: the encoding params of both encode and decode have to be compatible
encStr = str.encode(encoding='utf-16')
print(type(encStr))
print(encStr)
decStr = encStr.decode(encoding='utf-16') 
print(type(decStr))
print(decStr)

print(bytes("Hello",encoding='utf-16'))