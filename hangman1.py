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
#print splice[0:num_wrong_guesses]
body_parts = ['head','neck','torso','left arm','right arm','left leg','right leg']
allowed_guesses = len(body_parts)
cur_letter = ''
unguessed_letters = []
newword = ""

def init_word():
    f = open('/usr/share/dict/words')
    words = f.read()
    words = words.split('\n')
    myword = words[random.randint(0,len(words))]

    # 
    for i in myword:
        if i in special_chars:
            drawn_word.append(i)
        else:
            drawn_word.append("_")
            # only add letter once to unguessed_letters array!
            if i not in unguessed_letters:
                unguessed_letters.append(i)
    return myword

def init_game():
    theword = init_word()
    return theword

def print_progress():
    mline = "-" * 45
    l_num_wrong = "number wrong guesses: %d" % num_wrong_guesses
    l_wrong_chars = "wrong chars guessed:"
    print mline
    print l_num_wrong
    print mline
    print l_wrong_chars,",".join(wrong_chars)
    print mline
    if num_wrong_guesses:
        print body_parts[:num_wrong_guesses]

def ask_guess():
    cur_letter = raw_input('Guess a letter: ')
    while not test_letter(cur_letter):
        cur_letter = raw_input('Must be a single letter!!\n Guess a letter: ')
    check_letter(cur_letter)
    
def test_letter(ch):
    if (len(ch) > 1):
        return False
    else:
        return True

def check_letter(ch):
    global num_wrong_guesses
    if (ch in theword):
        correct_chars.append(ch)
        unguessed_letters.remove(ch)
        print "Unguessed: ","".join(unguessed_letters)
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
    print " ".join(newword)

theword = init_game()
#print theword


while mainloop:
    ask_guess()
    print_progress()
    if "_" not in newword:
        print "*" * 70
        print "You won!"
        mainloop = False
    else if num_wrong_guesses >= allowed_guesses:
        print "*" * 70
        print "You lose!  Game over, man!"
        main_loop = False

    #print theword
    #print drawn_word
    #mainloop = False
    
