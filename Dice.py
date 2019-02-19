# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:04:10 2019

@author: Balaji.B.R
"""

#importing radiant to selcet random variable
import random
import time #to keep process hold for sec
#Initializing the min and max values
min = 1
max = 6
i = 1
question = 'Do you like to roll the dice: y/n \n'
#requesting input for first time
ans = input(question)
#Logic to check the process
while (i==1):
    if (ans == 'y' or ans == 'Y'):
            print("Rolling the dice......")
            time.sleep(1)
            print("The number rolled to: ", random.randint(min,max))
            ans = input('Do you like to roll the dice again: y/n \n')
            continue
    elif(ans == 'n' or ans == 'N'):
        print('Game Over !! Thanks for playing')
        break
    elif(ans != 'y' or ans != 'Y' or ans != 'n' or ans != 'N'):
        print("Ivalid Response, Enter valid one y/n")
        ans=input("Enter your response: \n")
        continue
    