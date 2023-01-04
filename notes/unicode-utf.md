# Unicode and UTF-8  in Python
---

# ASCII
**American Standard Code for information Interchange** is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.

In python, the **org()** method tells us the numeric value of a simple ASCII character. Each character is represented by a number between 0 and 256 stored in 8 bits of memory

# Unicode
Unicode, formally The Unicode Standard, is an information technology standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems.

In Python 3, all strings internally are Unicode.

# Python Strings To Byte
When fetching data from a web server in python, you used the decode() method to convert it to string from bytes.

> bytes.decode(encoding="utf-8")
Returns a string decoded from the given bytes.

> str.encode(encoding="utf-8")
Returns an encoded version of the string as a byte object.

>Note: It's best practice to use the UTF-8 encoding because a character stored on the range of 1 - 4 byte.

# Reference
*ASCII*: [Wikipedia](https://en.wikipedia.org/wiki/ASCII)
*Unicode*: [Wikipedia](https://en.wikipedia.org/wiki/Unicode)
*PY4E*: [Video](https://www.youtube.com/watch?v=-cmlmaVSONg)
*Encoding*: [Python Docs](https://docs.python.org/3/library/stdtypes.html)