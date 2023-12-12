import art
from game_data import data
import random
#game_data contains a list of dictionaries

def get_celebs():
    random_num = random.randint(0,len(data))
    random_num2 = random.randint(0,len(data))
    if random_num == random_num2:
        get_celebs()
        #epic recursion moment
    celeb1 = data[random_num]
    celeb2 = data[random_num2]
    return(celeb1, celeb2)

def check_guess(guess, celeb1, celeb2):
    followers1 = celeb1['follower_count']
    followers2 = celeb2['follower_count']

    print(f"{celeb1['name']} has {followers1} followers.")
    print(f"{celeb2['name']} has {followers2} followers.")

    if (followers1 > followers2 and guess == 'A') or (followers2 > followers1 and guess == 'B'):
        print("You guessed correctly! You won!")
        return True
    else:
        print("Incorrect. You lose.")
        return False

score = 0
celeb1, celeb2 = get_celebs()

while True:
    print(art.logo)
    print(f"Current Score: {score}")
    print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}.")
    print(art.vs)
    print(f"Compare B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}.")
    guess = input("Who has more Instagram followers? Type 'A' or 'B':\n> ").upper()
    
    #we want the 2nd instagram account to be compared to a new randomly generated one,
    #only if there is a win
    if check_guess(guess, celeb1, celeb2):
        score += 1
        celeb1 = celeb2  
        celeb2 = random.choice(data)  
    else:
        print(f"Your final score is: {score}")
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break
        else:
            score = 0
            celeb1, celeb2 = get_celebs()  



