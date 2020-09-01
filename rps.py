#import modules
import random

# file i/o functions for historical results


def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history


def save_results(w, t, l):
    text_file = open("history.txt", "w")
    text_file.write(str(w) + "," + str(t) + "," + str(l))
    text_file.close()


# welcome message
results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[1])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

# initialize user, computer choices
computer = random.randint(1, 3)
user = input("[1] Rock [2] Paper [3] Scissors [9] Quit\n")
user = int(user)

# gameplay loop
while not user == 9:
    if user == 1:
        if computer == 2:
            print('Computer chose paper: You lose')
            losses += 1
        elif computer == 3:
            print('Computer chose scissors: You win!')
            wins += 1
        else:
            print('Tie!')
            ties += 1
    elif user == 2:
        if computer == 1:
            print('Computer chose rock: You Win!')
            wins += 1
        elif computer == 3:
            print('Computer chose scissors: You lose')
            losses += 1
        else:
            print('Tie!')
            ties += 1
    elif user == 3:
        if computer == 1:
            print('Computer chose rock: You lose')
            losses += 1
        elif computer == 2:
            print("Computer chose paper: You Win!")
            wins += 1
        else:
            print('Tie!')
            ties += 1

    else:
        print('Invalid selection. Please try again')
    # print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    # prompt user to make another choice
    print("Please choose to continue...")
    computer = random.randint(1, 3)
    user = input("[1] Rock [2] Paper [3] Scissors [9] Quit\n")
    user = int(user)

save_results(wins, ties, losses)
