print("\n" *15)
print("Welcome to Rock Trivia")
playing = input("Press y to play\n")
if playing.lower() != "y":
    print("FUCK YOU!")
    print("Type a y next time fucker")
    quit()
else:
    print("Good luck")

score = 0

answer = input("""What is Eddie Money's real name?
A) Greg Wilson B) Eddie Mahoney C) Eddie Money D) None of the Above
""")
if answer.lower() == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was B")

answer = input("""Who was Iron Maidnen's original singer?
A) Bill Ward B) John Elton C) Synyster Gates D) Paul DiAnno
""")
if answer.lower() == "d":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D")

answer = input("""Who was the drummer for Fleetwood Mac?
A) Rick Fleetwood B) Mac Fleetwood C) Mick Fleetwood D) Kenny Golladay
""")
if answer.lower() == "c":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C")

answer = input("""What year did Black Sabath's album Masters of Reality come out?
A) 1973 B) 1978 C) 1972 D) None of the Above
""")
if answer.lower() == "d":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D")

answer = input("""What does ELO stand for?
A) Enormous Light Organization B) Electric Light Orchestra C) Electriciy Limits Orders D) Excercise Loves Output
""")
if answer.lower() == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was B")

answer = input("""What band was Don Henley the lead singer of?
A) The Eagles B) Blue Oyster Cult C) Def Leppard D) The Cure
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was A")

answer = input("""Who was known as the leader of Motley Crue?
A) Nikki Sixx B) Tommy Lee C) Mick Mars D) Vince Neil
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was A")

answer = input("""Who was the guitarist for Rush?
A) Steve Perry B) Kenny Greg C) Eddie Stixx D) Alex Lifeson
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D")

answer = input("""What branch of the military was Jimmi Hendrix a part of?
A) Marines B) Navy C) Air Force D) Army
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D")

answer = input("""What city in the state of New York was Woodstock held in?
A) Albany B) Buffalo C) Bethel D) None of the above
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C")

answer = input("""What artist released Safety Dance?
A) Saving Keyes B) WHAM C) Men Without Hats D) Men at Work
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C")

answer = input("""What does WHAM stand for?
A) Wife Hates all Men B) We Hate Andrew's Mother C) What Happened at Midnight D) None of the Above
""")
if answer.lower() == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("The correct answer was B")

answer = input("""What city was famous guitarist Slash born in
A) Hampstead B) Paris C) Lyon D) Unknown
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    print("The correct answer was A")

answer = input("""Who was the original lead singer of Black Sabbath
A) Ronnie James Dio B) Ozzy Osbourne C) Ian Gillian D) Ray Gillen
""")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was B")

answer = input("""David Lee Roth was also know as: _____
A) Diamond Dave B) Dynamite Dave C) Super Dave D) Dyslexic Dave
""")
if answer == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was A")

answer = input("""What year did Pink Floyd release Dark Side of the Moon?
A) 1971 B) 1978 C) 1975 D) 1973
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was D")

answer = input("""This famous guitarist was tragically killed in a helicopter accident on August 27, 2018
A) Kurt Cobain B) Stevie Ray Vaughn C) Kobe Bryant D) Randy Rhoads
""")
if answer.lower() == "b":
    print("Correct!")
else:
    print("Incorrect. The correct answer is B")

answer = input("""In what Super Bowl did Prince perform the halftime show?
A) Super Bowl XL B) Super Bowl XLI C) Super Bowl XLII D) Super Bowl XLIV
""")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Prince performed the halftime show for Super Bowl XLI in Miami")
    print("The game was played on February 4, 2007. The Indianapolis Colts defeated the Chicago Bears 29-17")

answer = input("""What is the best selling album of all time? (As of January 25, 2023)
A) Rumours B) Thriller C) The Wall D) The Beatles
""")
if answer.lower() == "b":
    print("Correct!")
    print("'Thriller' is estimated to have sold 70 million copies worldwide")
    score += 1
else:
    print("Incorrect! The correct answer was B")

answer = input("""When was the Rock and Roll Hall of Fame established?
A) 1985 B) 1981 C) 1983 D) 1977
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was C")

answer = input("""Who was the drummer for Led Zepplin?
A) Jason Bonham B) Kenny Dixon C) Neil Peart D) John Bonham
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was D")

answer = input("""This band's drummer lost his arm in a car accident:
A) Def Leppard B) Metallica C) Poison D) Journey
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
    answer1 = input("What was his name?")
    if answer1 == "Rick Allen":
        print("Correct!")
        score =+ 2
else:
    print("Rick Allen was able to continue drumming for Def Leppard even after losing his arm.")

answer = input("""In what city was the movie Singles filmed?
A) Dallas B) Seattle C) New York D) Sacramento
""")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was B")

answer = input("""Who was the lead singer of The Doors?
A) Greg Hurts B) Roy Orbison C) Jim Morrison D) Van Morrison
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was C")

