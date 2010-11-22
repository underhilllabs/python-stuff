# decoder.py
# Decode secret messages!!
from string import split,join

def main():
    print "decoder: decode secret messages!"
    print

    message = raw_input("enter message to decode here ==> ")
    str_list = []
    for c in split(message):
        ascii_num = eval(c)
        str_list.append(chr(ascii_num))

    print join(str_list,"")

main()
