import random

def playgame():
    while True:
        try:
            low_limit=int(input("Enter a lower limit: "))
            high_limit=int(input("Enter a higher limit: "))
            if low_limit>=high_limit:
                print("Lower limit must be smaller than higher limit ")
            else:
                break
        except ValueError:
            print("Enter Valid Numbers Only!")
    
    num=random.randint(low_limit,high_limit)
    guess_count=0
    attempt_count=1
    
    print(f"I have selected number between {low_limit} and {high_limit}")
    while True:
        print(f"Attempt #{attempt_count}")
        
        try:
            guess=int(input("Guess The Number: "))
            
        except ValueError:
            print("INVALID - Enter A Number")  
            attempt_count+=1  
        else:
            if(guess<low_limit or guess>high_limit):
                print(f"Number must be between {low_limit} and {high_limit}")
                attempt_count+=1 
                
            elif(guess>num):
                print("Lower Number Please")
                guess_count+=1
                attempt_count+=1 
                
            elif(guess<num):
                print("Higher Number Please")
                guess_count+=1
                attempt_count+=1 

            elif guess == num:
                guess_count+=1
                break
              
    print(f"You guessed number {guess} correctly!")
    print(f"Total Attempts : {attempt_count}")
    print(f"Valid Guesses : {guess_count}")
    print("Congratulations! 🎉")
    choice = input("Restart game (y/n): ").lower()
    if(choice=="y"):
        return True
    elif(choice=="n"):
        return False
    else:
        print("Invalid Choice")
        return False



def main():
    print("GUESS THE NUMBER GAME")
    print("Welcome")
    
    choice = input("Begin game (y/n): ").lower()
    if(choice=="n"):
        print("Bye")
        return

    while True:
        restart = playgame()
        if restart==False:
            print("Thankyou")
            break


if __name__ == "__main__":
    main()





