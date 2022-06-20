import random
print("H A N G M A N")
victory = 0
lost = 0
def play_game():
    words = ["python", "java", "swift", "javascript"]
    word = random.choice(words)
    attempts = 8
    board = ["-" for item in range(len(word))]
    output_board = "".join(board)
    guesses = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        if attempts == 0:
            global lost
            lost += 1
            print()
            print("You lost!")
            break
        if "-" not in output_board:
            global victory
            victory += 1
            print("You guessed the word {}!".format(word))
            print("You survived!")
            break
        else:
            print()
            print(output_board)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("Please, input a single letter.")
            elif guess not in alphabet or guess.isupper():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif guess in guesses:
                print("You've already guessed this letter.")
            else:
                guesses.add(guess)
                if guess in word:
                    for i in range(len(word)):
                        if word[i] == guess:
                            board[i] = guess
                    output_board = "".join(board)
                else:
                    attempts -=1
                    print("That letter doesn't appear in the word.")
while True:
    option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if option == "play":
        play_game()
    elif option == "results":
        print("You won: {} times".format(victory))
        print("You lost: {} times".format(lost))
    elif option == "exit":
        break
