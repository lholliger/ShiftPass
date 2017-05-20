# -*- coding: utf-8 -*-
import string
import sys
current_arg_pos = 0

askpass = True
askstr = True
asktype = True
for x in sys.argv:
    if (x == "-e" or x == "--encrypt"):
        fc = "-e"
        asktype = False;
    if (x == "-d" or x == "--decrypt"):
        fc = "-d"
        asktype = False;
    if (x == "-p" or x == "--password"):
        askpass = False
        password = sys.argv[current_arg_pos+1]
    if (x == "-s" or x == "--string"):
        askstr = False
        tocrypt = sys.argv[current_arg_pos+1]

    if (x == "-h" or x == "--help"):
        print("""
        ShiftPass Encryption System by DatOneLefty

        help
        usage: python shiftpass [args]

        arguments:

        -e:              encrypt string
        -d:              decrypt string

        -p [password]   define password to use instead of asking in the script
        -s [string]     define string to use instead of asking in the script
        """)
    current_arg_pos = current_arg_pos + 1


if asktype == True:
        ect = raw_input("encrypt or decrypt (e/d): ")
        if (ect == "e"):
            fc = "-e"
        elif (ect == "d"):
            fc = "-d"
        else:
            sys.exit("invalid answer. must be e or d")


if askpass == True:
    password = raw_input("password: ")

if askstr == True:
    if (fc == "-e"):
        tocrypt = raw_input("string to encrypt: ")

    if (fc == "-d"):
        tocrypt = raw_input("string to decrypt: ")


cplace = -1
plen = len(password)

crypted = ""


all_string_pos = []
all_pass_pos = []
for pc in password:
    all_pass_pos.append(ord(pc))


for tc in tocrypt:
    all_string_pos.append(ord(tc))





pos = -1
for piece in all_string_pos:

    cplace = cplace + 1
    pos = pos + 1

    if cplace == plen:
        cplace = 0

    if fc == "-e":
        all_string_pos[pos] = all_string_pos[pos] + all_pass_pos[cplace]


    if fc == "-d":
        all_string_pos[pos] = all_string_pos[pos] - all_pass_pos[cplace]

if fc == "-e":
    for piece in all_string_pos:
        crypted = crypted + chr(piece)

if fc == "-d":
    for piece in all_string_pos:
        crypted = crypted + chr(piece)

if (fc == "-e"):
    print("Encrypted: " + crypted)

if (fc == "-d"):
    print("Decrypted: " + crypted)
