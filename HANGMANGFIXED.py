#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:17:07 2020

@author: ChristopherY.Sanchez
"""

sRealWord = input("Write the Hangman Word in Capital Letters: ") 
lShownWord = ["_"] * len(sRealWord) 
sInput = ""
Hint = input("Enter keyword or hint here: ")
iAllowedGuesses = 10  
iLetterNumber = 0   #was []
iRightGuesses = 0   #was [] 


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Let the Game Begin!")
print("Type END to close game, or complete your 10 guesses")

while(sInput != "END" and iAllowedGuesses != 0): 
    print("The word you're looking for is: " + str(lShownWord)) ##FIXED
    print("You have: " + str(iAllowedGuesses) + " guesses left") ##FIXED 
    print("Here is your hint: ", Hint)
    sInput = input("Enter letter in Capital Letters: ")
    iAllowedGuesses -= 1 ##VALUE 1 ##FIXED
   
  ###Used in this piece is the "for" loop combined with range.  
    for iLetterNumber in range(len(sRealWord)) : ###FIXED changed while for "for"
        if (sRealWord[iLetterNumber] == sInput) : ### and < for in and added range
            lShownWord[iLetterNumber] = sInput 
            iRightGuesses += 1    
         
    if (iRightGuesses == len(sRealWord)):  ###for different values.
            print("Woho!, You've won!")
            break
    if (iAllowedGuesses == 0):
            print("You are out of guesses, Game Over!") ###fixed
            break