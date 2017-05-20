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


chars = """ 1234567890-=QWERTYUIOP[]\ASDFGHJKLZXCVBNM,./qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+{}|:"<>?'"""

eb = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿ"

cplace = -1
plen = len(password)

crypted = ""


all_string_pos = []
all_pass_pos = []
for pc in password:
    posc = 0
    for p in chars:
        if p == pc:
            shift = posc
        posc = posc + 1

    all_pass_pos.append(shift)

if fc == "-e":
    for tc in tocrypt:
        posc = 0
        for p in chars:
            if p == tc:
                shift = posc
            posc = posc + 1
            all_string_pos.append(shift)

if fc == "-d":
    for tc in tocrypt:
        posc = 0
        for p in eb:
            if p == tc:
                shift = posc
            posc = posc + 1
            all_string_pos.append(shift)




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
        crypted = crypted + eb[piece]

if fc == "-d":
    for piece in all_string_pos:
        crypted = crypted + chars[piece]

if (fc == "-e"):
    print("Encrypted: " + crypted)

if (fc == "-d"):
    print("Decrypted: " + crypted)
