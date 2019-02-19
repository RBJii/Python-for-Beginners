# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:46:12 2019

@author: Balaji.B.R
"""
import random

def diff(c):
        if(c > 5):
            print("you are highly differenced")
        else:
            print("You are near to little difference") 

def guess(a, b):
    if(a>b):
        c= a -b
        diff(c)
    elif(b>a):
        c=b-a
        diff(c)


a = random.randint(0,9)
i = 1
print("I have generated a number from 0 to 9, Guess what it could be? \n")
b=int(input("Enter \n"))
while(i < 3):
    i=i+1
    print(i)
    if (a == b):
        print("Good you have guessed correctly within 3 guesses..Great Job !! The generated number is ", a)
        break
    else:
        guess(a, b)
        print("Guess once again")
        b=int(input("Enter \n"))
        continue
else:
    print("You lose all the three chances, sorry \n I generated the number:", a)            