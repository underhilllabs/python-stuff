# encoder.py
# encode messages with secret code

def main():
    print "Encoder: encode messages"
    print
    
    message = raw_input("Type message: ")
    for c in message:
        print ord(c),
    
    
    

main()
