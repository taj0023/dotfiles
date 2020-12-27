#!/usr/bin/env python3

word = 'undappori'
guessed = []
guessing = list('_' * len(word))
chance = 4

print("-------------------------------------")
while chance > 0:
    if "".join(guessing) == word:
        print("Yaaay.... U won!")
        break
    choice = input("enter choice: ")
    if choice in guessed:
        print("Already Guessed!")
        continue
    if choice in word:
        indexes = [i for i, c in enumerate(word) if c == choice]
        for index in indexes:
            guessing[index] = choice
        guessed.append(choice)
        print("Now : " + "".join(guessing) + "     Used Words : " + "".join(guessed))
        print("-------------------------------------")
    else:
        guessed.append(choice)
        print('guessed wrong!')
        print("Now : " + "".join(guessing) + "    Used Words : " + "".join(guessed))
        chance -= 1
        print("-------------------------------------")
        if chance == 0:
            print(f"You have failed this city...!! The answer was \"{word}\"")

