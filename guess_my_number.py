import random

LOW = 1
HIGH = 10

def generate_number():
    number = random.randint(LOW,HIGH)
    return number

def guess_the_number(num: int):
    greater = 0
    smaller = 0
    guess = -1
    while guess != num:
        guess = int(input("Guess a number: "))
        if guess < num:
            smaller += 1
            print("Incorrect, try again!")
        elif guess > num:
            greater += 1
            print("Incorrect, try again!")
    print(f"Congrats, you guessed it!\nNo. of too-high-guesses: {greater}\nNo. of too-low-guesses: {smaller}")
    
def main():
    num = generate_number()
    guess_the_number(num)

if __name__ == '__main__':
    main()
            
