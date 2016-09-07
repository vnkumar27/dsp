# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count  < 10:
        print 'Number of donuts: ' + str(count)
    else:
        print 'Number of donuts: Many'

def both_ends(s):
    if len(s) < 2:
        print ''
    else:
        print s[0]+s[1]+s[-2]+s[-1]

def fix_start(s):
    import re
    replaced = re.sub(s[0],'*',s)
    new_string = s[0]+replaced[1:]
    print new_string

def mix_up(a, b):
    print b[0:2]+a[2:]+ " "+ a[0:2]+b[2:]


def verbing(s):
	import re
    if len(s) >=3:
        if re.search("ing",s) == None:
            print s + "ing"
        else:
            print s + "ly"
    else:
        print s

def not_bad(s):
    punctuation =
    if s.find('not') < s.find('bad'):
        print s[:(s.find('not'))]+"good"
    else:
        print s


def front_back(a, b):
    if len(a)%2 == 0:
        fronta = a[:len(a)/2]
        backa = a[len(a)/2:]
    if len(b)%2 == 0:
        frontb = b[:len(b)/2]
        backb = b[len(b)/2]
    if len(a)%2 != 0:
        fronta = a[:len(a)/2 + 1]
        backa = a[len(a)/2+1:]
    if len(b)%2 != 0:
        frontb = b[:len(b)/2 + 1]
        backb = b[len(b)/2+1:]
    print fronta+frontb+backa+backb
    
    
    
    
    
    
    
    
    
    
    
    
    
