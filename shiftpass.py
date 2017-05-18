import string
import sys
tocrypt = raw_input("to encrypt: ")
password = raw_input("password: ");
chars = """ 1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+{}|:"<>?'"""

cplace = -1;
plen = len(password)

crypted = "";

try:
    sys.argv[1]
except:
    ect = raw_input("encrypt or decrypt (e/d): ")
    if (ect == "e"):
        fc = "-e"
    elif (ect == "d"):
        fc = "-d"
    else:
        sys.exit("invalid answer. must be e or d");
else:
    fc = sys.argv[1]

all_string_pos = [];
all_pass_pos = [];
for pc in password:
    posc = 0;
    for p in chars:
        if p == pc:
            shift = posc
        posc = posc + 1;

    all_pass_pos.append(shift);
for tc in tocrypt:
    posc = 0;
    for p in chars:
        if p == tc:
            shift = posc
        posc = posc + 1;
    all_string_pos.append(shift);




pos = -1;
for piece in all_string_pos:

    cplace = cplace + 1;
    pos = pos + 1;

    if cplace == plen:
        cplace = 0;

    if fc == "-e":
        all_string_pos[pos] = all_string_pos[pos] + all_pass_pos[cplace]
        if all_string_pos[pos] >= len(chars):
            goto = all_string_pos[pos] - len(chars)
            all_string_pos[pos] = goto


    if fc == "-d":
        all_string_pos[pos] = all_string_pos[pos] - all_pass_pos[cplace]
        if all_string_pos[pos] >= len(chars):
            goto = all_string_pos[pos] + len(chars)
            all_string_pos[pos] = goto

for piece in all_string_pos:
    crypted = crypted + chars[piece]


print crypted
