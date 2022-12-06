def questions():
    objectQ = input("Is it an object? [y/n] ").lower()
    print(">" + objectQ)

    if objectQ == "y":  # if it is an object
        eatQ = input("Can you eat it? [y/n] ").lower()
        print(">" + eatQ)

        if eatQ == "y":  # if the object is edible
            print("Eat it.")
            goodQ = input("Was it good? [y/n] ").lower()
            print(">" + goodQ)

            if goodQ == "y":  # if the edible object was good
                print("Wag your tail.")
                return
            if goodQ == "n":  # if the edible object was bad
                print("Puke it out.")
                print("Re-eat it.")
                return

        if eatQ == "n":  # if the object is not edible
            tennisQ = input("Is it a tennis ball? [y/n] ").lower()
            print(">" + tennisQ)

            if tennisQ == "y":  # if the inedible object is a tennis ball
                print("Pick it up.")
                print("Return to owner.")
                return
            if tennisQ == "n":  # if the inedible object is not a tennis ball
                print("Bark at it.")
                return

    if objectQ == "n":  # if it is not an object
        soundQ = input("Is it a sound? [y/n] ").lower()
        print(">" + soundQ)

        if soundQ == "y":  # if the intangible thing is a sound
            print("Bark at it.")
            return
        if soundQ == "n":  # if the intangible thing is not a sound
            print("Ignore it.")
            return


print("Start")
questions()
print("Done!")
