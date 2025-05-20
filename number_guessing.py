import random
import sys

def welcome_message():
    print("Welcome to Number Guessing Game")

def generate_random_number(user_difficulty_level):
    if user_difficulty_level == 1:
        number, max_tries = random.randint(1, 50), 5
    elif user_difficulty_level == 2:
        number, max_tries = random.randint(1, 100), 7
    elif user_difficulty_level == 3:
        number, max_tries = random.randint(1, 1000), 10
    return number, max_tries

def get_user_input():
    user_input = int(input("Enter your guess : "))
    return user_input

def check_equality(user_input, random_number):
    status = False
    if user_input > random_number:
        print("Your Guess is Higher")
    elif user_input < random_number:
        print("Your Guess is Lower")
    elif user_input == random_number:
        print("You have Won !!!")
        status = True
    return status

def get_difficulty_levels():
    print("Difficulty Levels : \n")
    print("1: Easy 1-50")
    print("2: Medium 1- 100")
    print("3: Hard 1- 1000")
    user_difficulty_level = int(input("Enter your difficulty level : "))
    return user_difficulty_level

def wanna_retry():
    user_wish = input("Do you want to re play the game ? (yes/no) : ")
    if user_wish == "yes":
        main()
    else:
        print("Thanks for Playing the Game !!! Will Meet you Soon")

def play(random_number, max_tries):
    status = False
    atempts = 0
    while not status:
        if atempts > max_tries:
            print("You have exceeded MAX Attempts !! Try Again !!! ")
            break
        atempts = atempts + 1
        user_input = get_user_input()
        status = check_equality(user_input, random_number)
        if status == True:
            save_leaderboard(atempts)

def save_leaderboard(attempts):
    result = {}
    with open("guess_leaderboard.txt", "r") as file:
        winners = file.readlines()
    for person in winners:
        name, score = person.split("||")
        result[name] = score
    
    name = input("Please enter your name for Leaderboard : ")
    result[name] = 1000 - ((attempts - 1) * 100)

    with open("guess_leaderboard.txt", "w") as file:
        for name, score in result.items():
            file.write(f"{name}||{score}\n")
    print("Score added to Leaderboard")

def list_leaderboard():
    with open("guess_leaderboard.txt", "r") as file:
        winners = file.readlines()
    for person in winners:
        name, score = person.split("||")
        print(name, score)
        

def main():
    welcome_message()
    user_difficulty_level = get_difficulty_levels()
    random_number, max_tries = generate_random_number(user_difficulty_level)
    print(random_number)
    play(random_number, max_tries)
    wanna_retry()
    # print(random_number, type(random_number))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        list_leaderboard()
    else:
        main()