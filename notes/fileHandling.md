# File Handling
---

In python, file handling is performed using the ***Open()*** method. Which takes in two arguments
**filepath** & **mode**.

Open(filepath,mode[optional])
* Filepath/Filename: The location of the file
* Mode: Have two values which are 'r' and 'w' (R- reading and W-writing)

---

>## File Handling
File handling is an integral part of programming. File handling in Python is simplified with built-in methods, which include creating, opening, and closing files. While files are open, Python additionally allows performing various file operations, such as reading, writing, and appending information(Google).

>## Handle
When Using The Open Method, its creates a variable which serves as a Handle.
A Handle isn't the file, It's just an intermediary that allows you make changes on that file.


```
txtf = open('file.txt')

for line in txtf:
    print(line)


```

