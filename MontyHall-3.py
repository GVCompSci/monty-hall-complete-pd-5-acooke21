'''
Created on Jan 7, 2019

@author: Lexi Cooke
Monty Hall 
3. Building the Simulation
'''

from random import randint


win = 0
count = 0
print("Between 10 and 10,000:")
rounds = int(input("How many rounds of the game would you like to be simulated?: "))
while rounds > 10000 or rounds < 10:
    print("Must enter a number between 10 and 10000")
    rounds = int(input("Please try again: "))

answer = input("Should the player switch or stay?: ")
while answer != 'switch' and answer != 'stay':
    print('Must enter either "switch" or "stay"')
    answer = input("Please try again: ")

for run in range(rounds):
    door = randint (1,3)
    guess = randint (1,3)
    if answer == 'stay':
        if guess == door:
            win += 1
            count += 1
        else:
            win = win
            count += 1
    elif answer == 'switch':
        if guess == 1:
            guess = randint (2,3)
            if guess == door:
                win += 1
                count += 1
            else:
                win = win
                count += 1
        elif guess == 2:
            someVar = randint (1,2)
            if(1):
                guess = 1
            elif(2):
                guess = 3
            if guess == door:
                win += 1
                count += 1
            else:
                win = win
                count += 1
        else:
            guess = randint (1,2)
            if guess == door:
                win += 1
                count += 1
            else:
                win = win
                count += 1
if rounds == count:
    print(' ', end = '')
    
percent = win/rounds
percent *= 100             
print("The player won ",win,"/",rounds," games (",format(percent, '>0.2f'),"%)")
             
