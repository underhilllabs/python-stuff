#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import random,re
from string import maketrans

mainloop = True
theword = ""
num_wrong_guesses = 0
guesses = []
wrong_chars = []
correct_chars = []
drawn_word = []
# add special characters here
special_chars = "'é"
body_parts = ['head','torso','left arm','right arm','left leg','right leg']
allowed_guesses = len(body_parts)
cur_letter = ''
unguessed_letters = []
newword = ""
w = []

w.append( """
    _________
    |         |
    |        
    |       
    |       
    |
    |

""")

w.append("""
    _________
    |         |
    |         0
    |  
    |   
    |
    |

""")


w.append("""
    _________
    |         |
    |         0
    |         |
    |         
    |
    |

""")

w.append("""
    _________
    |         |
    |         0
    |        /|
    |        
    |
    |

""")

w.append("""
    _________
    |         |
    |         0
    |        /|\  
    |          
    |
    |

""")

w.append("""
    _________
    |         |
    |         0
    |        /|\ 
    |        /   
    |
    |

""")

w.append("""
    _________
    |         |
    |         0
    |        /|\ 
    |        / \ 
    |
    |

""")


def init_word():
    global newword
    f = open('/usr/share/dict/words')
    words = f.read()
    words = words.split('\n')
    myword = words[random.randint(0,len(words))]
    #myword = myword.lower()
    newword = "_" * len(myword)

    for i in myword:
        if i in special_chars:
            drawn_word.append(i)
        else:
            drawn_word.append("_")
            # only add letter once to unguessed_letters array!
            if i not in unguessed_letters:
                unguessed_letters.append(i)
        
    return myword.lower()

def init_game():
    theword = init_word()
    return theword

def print_progress():
    mline = "-" * 45
    l_num_wrong = "number wrong guesses: %d" % num_wrong_guesses
    l_wrong_chars = "wrong chars guessed:"
    print mline, "\n", "\n"
    print l_wrong_chars,",".join(wrong_chars)
    #if num_wrong_guesses:
    #    print body_parts[:num_wrong_guesses
    print "\n"," ".join(newword)
    print w[num_wrong_guesses]

def ask_guess():
    cur_letter = raw_input('Guess a letter: ')
    while not test_letter(cur_letter):
        cur_letter = raw_input('Guess a letter: ')
    check_letter(cur_letter)
    
def test_letter(ch):
    if ch in guesses:
        print "you've already guessed %s" % ch
        return False
    elif len(ch) > 1 or len(ch) < 1:
        print "Enter a single character!"
        return False
    else:
        return True

def check_letter(ch):
    global num_wrong_guesses
    guesses.append(ch)
    if (ch in theword):
        correct_chars.append(ch)
        unguessed_letters.remove(ch)
        #print "Unguessed: ","".join(unguessed_letters)
        print ch, " is correct!"
        print "Correct letters: ",
        print ",".join(correct_chars)
        add_word_char(ch)
    else:
        print ch, " is incorrect!"
        num_wrong_guesses += 1
        wrong_chars.append(ch)
        print "You have made %d wrong guesses" % num_wrong_guesses
        print ",".join(wrong_chars)
        
def add_word_char(ch):
    global newword
    """ we are grabbing the unguessed letters, 
    replacing them with an underscore in the 
    and returning the word
    """
    intab = "".join(unguessed_letters)
    outtab = "_" * len(intab)
    trantab = maketrans(intab,outtab)
    newword = theword
    newword = newword.translate(trantab)

     
theword = init_game()

while mainloop:
    ask_guess()
    print_progress()
    if "_" not in newword:
        print "*" * 70
        print "You won!"
        mainloop = False
    elif num_wrong_guesses >= allowed_guesses:
        print "*" * 70
        print "You lose!  Game over, man!"
        print "Correct word: %s" % theword
        mainloop = False

    #print theword
    #print drawn_word
    #mainloop = False
    



