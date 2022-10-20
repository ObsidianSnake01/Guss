def vroom():
    class Person:
        def __init__(self, name):
            self.name = name

        def talk(self):
            print(f"Hi, I am {self.name} how are you?  ")


    ryan = Person("Ryan Choister")
    print(ryan.name)
    ryan.talk()
    print("welcome to the car game!")
    command = ""
    started = False
    Parked = False
    Horn = True
    while command != "quit":
        command = input("-> ").lower()
        if command == "start":
            if started:
                print("car has already started")
            elif Parked:
                print("Backing out...")
            else:
                started = True
                for item in [3, 2, 1, "Go!"]:
                    print(item)
                print("Car started...")
        elif command == "stop":
            if not started:
                print("Car is already stopped!")
            elif Parked:
                print("The car is already parked")
                if Horn:
                    print("Beeeeeeeeeeep")
            else:
                started = False
                print("Car stopped.")
        elif command == "drive":
            Parked = False
            if started:
                print("going forward")
            else:
                print("Car hasn't started.")
        elif command == "turn left":
            if started:
                print("turning left!")
            elif Parked:
                print("car parked")
            else:
                print("Car not started!")
        elif command == "turn right":
            if started:
                print("turning right!")
            else:
                print("Car not started")
        elif command == "arrive":
            if Parked:
                print("You have arrived at your destination")
            else:
                print("Welcome")
        elif command == "park":
            Parked = True
            if started:
                print("backing up...")
            elif Parked:
                print("Car parked! Cya!")
            else:
                print("Car stopped!")
        elif command == "back":
            if started:
                print("backing up!")
            elif Parked:
                print("Car is parked please start the car!")
            else:
                print("Car not started")
        elif command == "good":
            print("Good thanks!")
        elif command == ":)":
            print("Happy!")
        elif command == "story":
            print("Choister looked at the ripped hat in his hands and felt sad.\n He walked over to the window and reflected on his sketchy surroundings.\n He had always loved glamorous Idaho with its bumpy, boiled Big city.\n It was a place that encouraged his tendency to feel sad.\n Then he saw something in the distance, or rather someone.\n It was the figure of Dennis The Menace.\n Dennis was a patient monster with solid hands and handsome eyes.gulped.\n He glanced at his own reflection.\n He was a cold-blooded, selfish, coffee drinker with tall hands and strong eyes.\n His friends saw him as a horrible, hard hero.\n Once, he had even helped a weary baby bird cross the road.\n But not even a cold-blooded person who had once helped a weary baby bird cross the road, was prepared for what Dennis had in store today.\n The snow flurried like cooking snakes, making cross.\n As stepped outside and Dennis came closer, he could see the giant glint in his eye.\n I am here because I want revenge, Dennis bellowed, in a scheming tone. He slammed his fist against 's chest, with the force of 4381 foxes. I frigging hate you, Choister.\n looked back, even more cross and still fingering the ripped hat. Dennis, my friend, he replied.\n They looked at each other with confident feelings, like two gifted, gentle goldfish talking at a very intelligent snow storm, which had classical music playing in the background and two malicious uncles thinking to the beat.\n studied Dennis's solid hands and handsome eyes. Eventually, he took a deep breath.\n I'm sorry, but I can't give you revenge, he explained, in pitying tones.\n Dennis looked calm, his body raw like a happy, heavy hawk.\n could actually hear Dennis's body shatter into 4702 pieces.\n Then the patient monster hurried away into the distance.\n Not even a cup of coffee would calm 's nerves tonight.\n THE END")
        elif command == "help":
            print("""
    start - to start the car
    turn left or right - to turn
    stop - to stop car
    drive - to go forward
    arrive - your here!
    park - to park?
    quit - to quit
    good - message
    story - prints a story
            """)
        elif command == "quit":
            while True:
                answer = input('Do you want to continue?:')
                if answer.lower().startswith("y"):
                        print("ok, carry on then")
                        vroom()
                elif answer.lower().startswith("n"):
                    sanswer = input("Do you want to play the guessing game? ")
                    if sanswer.lower().startswith("y"):
                        import guess2
                    else:
                        exit()
        else:
            print("Sorry, you cant do that!")
#where code starts
vroom()
