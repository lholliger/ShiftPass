import string
import sys
current_arg_pos = 0
import binascii

current_version = "01" # THIS CHANGES WITH EVERY ENCODING UPDATE TO PREVENT ERRORS

askpass = True
askstr = True
asktype = True
force = False
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

    if (x == "-f" or x == "--force"):
        force = True

    if (x == "-h" or x == "--help"):
        print("""
        ShiftPass Encryption System by DatOneLefty

        help
        usage: python shiftpass [args]

        arguments:

        -e:              encrypt string
        -d:              decrypt string
        -f:              force decoding an older version

        -p [password]   define password to use instead of asking in the script
        -s [string]     define string to use instead of asking in the script
        """)
    current_arg_pos = current_arg_pos + 1


if asktype == True:
        ect = input("encrypt or decrypt (e/d): ")
        if (ect == "e"):
            fc = "-e"
        elif (ect == "d"):
            fc = "-d"
        else:
            sys.exit("invalid answer. must be e or d")


if askpass == True:
    password = input("password: ")

if askstr == True:
    if (fc == "-e"):
        tocrypt = input("string to encrypt: ")

    if (fc == "-d"):
        tocrypt = input("string to decrypt: ")

if (fc == "-d"):
    enc1 = tocrypt;
    tocrypt = enc1.split("=")[1]
    version = enc1.split("=")[0]
    tocrypt = binascii.unhexlify(tocrypt).decode('utf8')

    if (force == False):
        if (version != current_version):
            sys.exit("Fatal Error: the string to decrypt was encrypted using an old version and will not work! add -f to the command to force decoding");


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
        all_string_pos[pos] = (all_string_pos[pos] + all_pass_pos[cplace]) % 255
    if fc == "-d":
        all_string_pos[pos] = (all_string_pos[pos] - all_pass_pos[cplace]) % 255

if fc == "-e":
    for piece in all_string_pos:
        crypted = crypted + chr(piece)

if fc == "-d":
    for piece in all_string_pos:
        crypted = crypted + chr(piece)

if (fc == "-e"):
    print("01=" + binascii.hexlify(crypted.encode('utf8')).decode("utf-8"))

if (fc == "-d"):
    print(crypted)
