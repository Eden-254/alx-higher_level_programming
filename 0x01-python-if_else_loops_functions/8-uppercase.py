#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in range(len(str)):
        if (ord(str[c]) >= 97 and ord(str[c]) <= 122):
            new_str += chr(ord(str[c]) - 32)
            continue
            new_str += str[c]

        print('{0}'.format(new_str))
