def main():
    import random

    try:
        limit = int(input("How many guesses do you want: "))
    except ValueError:
        print("Invalid Value")
        main()
    if limit > 50:
        print("You cant use any number over 50")
        main()
    elif limit <= 0:
        print("No numbers under 1")
        main()

    score = 0
    number = random.randint(1, 50)
    Guess_count = 0
    guess_limit = int(limit)
    while True:
        while Guess_count < guess_limit:
            try:
                guess = int(input("Guess: "))
                Guess_count += 1
            except ValueError:
                print("Invalid Value")
                try:
                    limit = int(input("How many guesses do you want: "))
                except ValueError:
                    print("Invalid Value")
                    main()
                score = 0
                number = random.randint(1, 50)
                Guess_count = 0
                guess_limit = int(limit)
                while Guess_count < guess_limit:
                    try:
                        guess = int(input("Guess: "))
                        Guess_count += 1
                    except ValueError:
                        print("Invalid Value")
                        main()
                    if guess > 50:
                        print("No numbers above 50")
                        if Guess_count <= 1:
                            Guess_count = 0
                        elif Guess_count < 0:
                            Guess_count -= 1
                    elif guess == number:
                        print('You Won!')
                        score += 1
                        print("You got it in", Guess_count, "guesses")
                        if 0 < score <= 1:
                            print("You have", score, "win!")
                        else:
                            print("You have", score, "wins!")
                        redo = input("Want to play again? ").lower()
                        if redo.lower().startswith("y"):
                            print("Good luck!\n")
                            main()
                        else:
                            again = input("Want to play the car game? ")
                            if again.lower().startswith("y"):
                                import cargm
                            else:
                                print("Good bye!")
                                exit()
                    elif guess > number:
                        print("You were above the number!")
                        print("You have guessed", Guess_count, "times")
                    else:
                        print("You were below the number!")
                        print("You have guessed", Guess_count, "times")
                else:
                    print('sorry, you lost')
                    print("The number was", number)
                    try_again = input("Want to try again: ").lower()
                    if try_again.lower().startswith("y"):
                        print("Good luck!")
                        main()
                    elif try_again.lower().startswith("n"):
                        new_game = input("want to play the car game: ").lower()
                        if new_game.lower().startswith("y"):
                            permis = input("Do you have parental permission to play the guessing game")
                            if permis.lower().startswith("y"):
                                import cargm
                            else:
                                print("Good bye!")
                                exit()
                        elif try_again.lower().startswith("n"):
                            print("Good bye!")
                            exit()

                    else:
                        print("Good bye!")
                        exit()
            if guess == number:
                print('You Won!')
                score += 1
                print("You got it in", Guess_count, "guesses")
                if 0 < score <= 1:
                    print("You have", score, "win!")
                else:
                    print("You have", score, "wins!")
                redo = input("Want to play again? ").lower()
                if redo.lower().startswith("y"):
                    print("Good luck!\n")
                    main()
                else:
                    again = input("Want to play the car game? ")
                    if again.lower().startswith("y"):
                        import cargm
                    else:
                        print("Good bye!")
                        exit()
            elif guess > number:
                print("You were above the number!")
                print("You have guessed", Guess_count, "times")
            else:
                print("You were below the number!")
                print("You have guessed", Guess_count, "times")
        else:
            print('sorry, you lost')
            print("The number was", number)
            try_again = input("Want to try again: ").lower()
            if try_again.lower().startswith("y"):
                print("Good luck!")
                main()
            elif try_again.lower().startswith("n"):
                new_game = input("want to play the car game: ").lower()
                if new_game.lower().startswith("y"):
                    permis = input("Do you have parental permission to play the guessing game")
                    if permis.lower().startswith("y"):
                        import cargm
                    else:
                        print("Good bye!")
                        exit()
                elif try_again.lower().startswith("n"):
                    print("Good bye!")
                    exit()

            else:
                print("Good bye!")
                exit()


# where main ends
# where begin starts
def begin():
    try:
        birth_year = input("What year were you born? ")
        age = 2022 - int(birth_year)
        age2 = 2021 - int(birth_year)
        print("That means you are ", age, "or", age2, "years old")
    except ValueError:
        print("Invalid value")
        begin()

    if 130 > int(age) > 18:  # if the age is under 130 and above 18
        if age > 100:  # if age is above 100 but below 130
            ua = input("Are you sure that is your real age? ")
            if ua.lower().startswith("y"):
                try:
                    print("Then please answer this question")
                    check = input("L or M: ")
                except ValueError:
                    print("Invalid value")
                if check.lower().startswith("m"):
                    print("\nYour answer was incorrect you will now play the car game\n")
                    import cargm
                elif check.lower().startswith("l"):
                    print("You're in.")
                    print('\nWelcome to the guessing game!\n')
                    print('Guess a number between 1 and 50!\n')
                    main()
                else:
                    print("Please enter in L or M")
            elif ua.lower().startswith("n"):
                seca = input("\nPlease enter in your real age: ")
                if int(seca) > 130:
                    print("Then please answer this question")
                    check = input("L or M: ")

                    if check.lower().startswith("m"):
                        print("\nYour answer was incorrect you will now play the car game\n")
                        import cargm
                    elif check.lower().startswith("l"):
                        print("You're in.")
                        print('\nWelcome to the guessing game!\n')
                        print('Guess a number between 1 and 50!\n')
                        main()
            else:
                print("please enter in y or n")
                smalls()
        print("You're in.")
        print('\nWelcome to the guessing game!\n')
        print('Guess a number between 1 and 50!\n')
        main()
    elif 0 < int(age) < 18:
        print("You're not allowed here.\n", "This game is for people 18+")  # Cg is car game
        cg = input("Do you want to play the car game? ")
        if cg.lower().startswith("y"):
            import cargm
        else:
            print("Goodbye!")
            exit()
    elif int(age2) > 130:
        print("Please enter yor real age!")
        begin()
    else:
        print("No negative numbers enter in a number less than 2023")
        begin()


# code really starts!
begin()

try:
    birth_year = input("What is year were you born? ")
    age = 2022 - int(birth_year)
    age2 = 2021 - int(birth_year)
    print("That means you are ", age, "or", age2, "years old")
except ValueError:
    print("Invalid value")
    begin()


def smalls():
    if 130 > int(age) > 18:
        if age > 100:
            ua = input("Are you sure that is your real age? ")
            if ua.lower().startswith("y"):
                print("Then please answer this question")
                check = input("L or M: ")
                if check.lower().startswith("m"):
                    print("\nYour answer was incorrect you will now play the car game\n")
                    import cargm
                elif check.lower().startswith("l"):
                    print("You're in.")
                    print('\nWelcome to the guessing game!\n')
                    print('Guess a number between 1 and 50!\n')
                    main()
            elif ua.lower().startswith("n"):
                seca = input("\nPlease enter in your real age: ")
                if int(seca) > 130:
                    print("Then please answer this question")
                    check = input("L or M: ")

                    if check.lower().startswith("m"):
                        print("\nYour answer was incorrect you will now play the car game\n")
                        import cargm
                    elif check.lower().startswith("l"):
                        print("You're in.")
                        print('\nWelcome to the guessing game!\n')
                        print('Guess a number between 1 and 50!\n')
                        main()
            else:
                print("please enter in y or n")
                begin()
        print("You're in.")
        print('\nWelcome to the guessing game!\n')
        print('Guess a number between 1 and 50!\n')
        main()
    elif 0 < int(age) < 18:
        print("You're not allowed here.\n", "This game is for people 18+")  # Cg is car game
        cg = input("Do you want to play the car game? ")
        if cg.lower().startswith("y"):
            import cargm
        else:
            print("Goodbye!")
            exit()
    elif int(age2) > 130:
        print("Please enter yor real age!")
        begin()
    else:
        print("No negative numbers enter in a number less than 2023")
        begin()
