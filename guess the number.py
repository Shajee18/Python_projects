import random
print("welcome to number guessing game!")
while True:
    secret =  random.randint(1,100)
    attempts = 0

    while True:
        num = int(input("guess a number between 1 to 100:" ))
        attempts +=1

        if num > secret :
            print("to high! try again")

        elif num < secret :
            print("to low!try again ")

        else:
            print("you guessed it right in",attempts,"attempts!!" )  
            
            break  
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break

 
