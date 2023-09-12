import random
import turtle

# list of words to choose from
words = ["akbar", "nigga", "shit", "vape", "edible", "weed", "carlos"]

# choose a word randomly
word = random.choice(words)

# set up variables
guesses = []
max_fails = 6
fails = 0

# set up turtle screen
screen = turtle.Screen()
screen.title("Hangman")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# set up turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(-200, -200)

# draw the gallows
pen.pendown()
pen.forward(200)
pen.backward(100)
pen.left(90)
pen.forward(300)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)

# draw the man
man = turtle.Turtle()
man.speed(0)
man.penup()
man.hideturtle()
man.goto(-100, -50)
man.pendown()

# main loop
while True:
    # print the current state of the word
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    
    # ask the player to guess a letter
    guess = screen.textinput("Guess a letter", "Guess a letter: ").lower()
    
    # check if the letter has already been guessed
    if guess in guesses:
        print("You already guessed that letter.")
        continue
    
    # add the guess to the list of guesses
    guesses.append(guess)
    
    # check if the guess is correct
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect.")
        fails += 1
        if fails == 1:
            # draw the head
            man.circle(20)
        elif fails == 2:
            # draw the body
            man.right(90)
            man.forward(50)
        elif fails == 3:
            # draw the left arm
            man.backward(20)
            man.left(45)
            man.forward(30)
        elif fails == 4:
            # draw the right arm
            man.backward(30)
            man.right(90)
            man.forward(30)
        elif fails == 5:
            # draw the left leg
            man.backward(30)
            man.left(45)
            man.forward(50)
        else:
            # draw the right leg and end the game
            man.backward(50)
            man.right(90)
            man.forward(50)
            print("Sorry, you lose. The word was", word)
            break
    
    # check if the player has won
    if set(word) == set(guesses):
        print("Congratulations, you win!")
        break

# display the turtle screen
turtle.done
