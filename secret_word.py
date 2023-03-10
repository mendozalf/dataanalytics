#Secret Word Game

import time

#inputs

name = input('What is your name? ')

print(f'Hi {name}, is time to guess the secret word')

time.sleep(1)

secret_word = "temple"

guess_count = 0

guesses = -1

your_guess = ""

#for and while loops

for x in secret_word:
        
        print("_ ", end='')
print("\n")   

while your_guess != secret_word:
     
    your_guess = input('What is your guess? ')
    if len(your_guess) > len(secret_word) or len(your_guess) < len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word")
        guess_count +=1

    else:    
        if your_guess.lower() == secret_word:
            print("Congratulations! You won!")
        else:
                  
            for y in your_guess:
                if y in secret_word and y not in your_guess: 
                    print( y, end=' ' )
                elif y in secret_word and y in your_guess: 
                    print( y.upper(), end=' ' )
                else:
                    print("_ ", end='')
            print("\n") 
        guess_count +=1                 
            

#game over

print('You guessed it!')
print(f"It took you {guess_count} guesses")
