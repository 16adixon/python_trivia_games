print("Welcome to NFL Trivia")

score = 0

seahawks_punters = [
    "Jon Ryan", "Rick Tuten", "Michael Dickson", "Jeff Feagles", "Jeff West", "Herman Weaver", "Ruben Rodriguez", "Ryan Plackemeier", "Tom Rouen", "Rick Donnelly", "Rick Engles", "Vince Gamache", "Dave Finzer", "Donnie Jones", "Ken Walter", "Rohn Stark", "Leo Araguz", "Jimmy Colquitt", "Alex Waits", "Russ Griffith", "Kyle Richardson", "Efren Herrera", "Barry Bowman", "Josh Brown", "Frank Garcia", "Dan Doornink", "Olindo Mare"
]
seahawks_punters.remove("John Ryan")
seahawks_punters.remove("Michael Dickson")

# answer = input("""What college did former Seahawks kicker Rian Lindell attend?
# A) LSU B) University of Washington C) LSU D) WSU
# """)
# if answer.lower() == "Rian Lindell":
#     print("Correct!\n")
#     score += 1
# else:
#     print("Incorrect! The correct answer was __\n")

answer1 = input("""Marcus Trufant was selected by the Seattle Seahawks in the first round of the 2003 NFL Draft. What overall pick?
A) 10th B) 13th C) 32nd D) 11th
""")
if answer1.lower() == "d":
    print("Correct!\n")
    score += 1
    answer2 = input("When was his last season with the Seahawks?")
    if answer2 == "2012":
        print("Correct!")
    answer3 = input("How many brothers does Marcus have? Please type your answer")
    if answer3.lower == "two":
        print("Correct!")
    else:
        print("Incorrect!")
else:
    print("Incorrect! The correct answer was D\n")

answer = input("""This quarterback was drafted 2nd overall in the ______ NFL draft
A)  B)  C)  D)
""")
if answer.lower() == "__":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was __\n")

answer = input("""On 
A)  B)  C)  D)
""")
if answer.lower() == "__":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was __\n")

answer = input("""WSU played its first Rose Bowl on what date?
A) January 1st, 1916 B)  C)  D) 
""")
if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was A\n")

