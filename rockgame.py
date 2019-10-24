import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if comp == 'rock' and user == 'scissors':
        print(f"Comp {comp} wins over user {user}")

    if comp == 'paper' and user == 'rock':
        print(f"Comp {comp} wins over user {user}")

    if comp == 'scissors' and user == 'paper':
        print(f"Comp {comp} wins over user {user}")
    
    if user == 'rock' and comp == 'scissors':
        print(f"User {user} wins over comp {comp}")

    if user == 'paper' and comp == 'rock':
        print(f"User {user} wins over comp {comp}")
    
    if user == 'paper' and comp == 'rock':
        print(f"User {user} wins over comp {comp}")

    if user == 'paper' and comp == 'paper':
        print(f"It's a draw")
    
    if user == 'rock' and comp == 'rock':
        print(f"It's a draw")

    if user == 'scissors' and comp == 'scissors':
        print(f"It's a draw")
    
#test
rps()