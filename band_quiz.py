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

#question 1
answer = input("""What is Eddie Money's real name?
A) Greg Wilson B) Eddie Mahoney C) Eddie Money D) None of the Above
""")
if answer.lower() == "b":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was B\n")

answer = input("""Who was Iron Maidnen's original singer?
A) Bill Ward B) John Elton C) Synyster Gates D) Paul DiAnno
""")
if answer.lower() == "d":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D\n")

answer = input("""Who was the drummer for Fleetwood Mac?
A) Rick Fleetwood B) Mac Fleetwood C) Mick Fleetwood D) Kenny Golladay
""")
if answer.lower() == "c":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C\n")

answer = input("""What year did Black Sabath's album Masters of Reality come out?
A) 1973 B) 1978 C) 1972 D) None of the Above
""")
if answer.lower() == "d":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D\n")

#question 5
answer = input("""What does ELO stand for?
A) Enormous Light Organization B) Electric Light Orchestra C) Electriciy Limits Orders D) Excercise Loves Output
""")
if answer.lower() == "b":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was B\n")

answer = input("""What band was Don Henley the lead singer of?
A) The Eagles B) Blue Oyster Cult C) Def Leppard D) The Cure
""")
if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was A\n")

answer = input("""Who was known as the leader of Motley Crue?
A) Nikki Sixx B) Tommy Lee C) Mick Mars D) Vince Neil
""")
if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was A\n")

answer = input("""Who was the guitarist for Rush?
A) Steve Perry B) Kenny Greg C) Eddie Stixx D) Alex Lifeson
""")
if answer.lower() == "d":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D\n")

answer = input("""What branch of the military was Jimmi Hendrix a part of?
A) Marines B) Navy C) Air Force D) Army
""")
if answer.lower() == "d":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was D\n")

#question 10
answer = input("""In what city in the state of New York was Woodstock held?
A) Albany B) Buffalo C) Bethel D) None of the above
""")
if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C\n")

answer = input("""What artist released Safety Dance?
A) Saving Keyes B) WHAM C) Men Without Hats D) Men at Work
""")
if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer was C\n")

answer = input("""What does WHAM stand for?
A) Wife Hates all Men B) We Hate Andrew's Mother C) What Happened at Midnight D) None of the Above
""")
if answer.lower() == "b":
    print("Correct\n")
    score += 1
else:
    print("Incorrect")
    print("The correct answer was B\n")

answer = input("""What city was famous guitarist Slash born in
A) Hampstead B) Paris C) Lyon D) Unknown
""")
if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect")
    print("The correct answer was A\n")

answer = input("""Who was the original lead singer of Black Sabbath
A) Ronnie James Dio B) Ozzy Osbourne C) Ian Gillian D) Ray Gillen
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

#question 15
answer = input("""David Lee Roth was also know as: _____
A) Diamond Dave B) Dynamite Dave C) Super Dave D) Dyslexic Dave
""")
if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was A\n")

answer = input("""What year did Pink Floyd release Dark Side of the Moon?
A) 1971 B) 1978 C) 1975 D) 1973
""")
if answer.lower() == "d":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was D\n")

answer = input("""This famous guitarist was tragically killed in a helicopter accident on August 27, 2018
A) Kurt Cobain B) Stevie Ray Vaughn C) Kobe Bryant D) Randy Rhoads
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is B\n")

answer = input("""In what Super Bowl did Prince perform the halftime show?
A) Super Bowl XL B) Super Bowl XLI C) Super Bowl XLII D) Super Bowl XLIV
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")
    print("Prince performed the halftime show for Super Bowl XLI in Miami")
    print("The game was played on February 4, 2007. The Indianapolis Colts defeated the Chicago Bears 29-17\n")

answer = input("""What is the best selling album of all time? (As of January 25, 2023)
A) Rumours B) Thriller C) The Wall D) The Beatles(Self Titled)
""")
if answer.lower() == "b":
    print("Correct!")
    print("'Thriller' is estimated to have sold 70 million copies worldwide\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

#question 20
answer = input("""When was the Rock and Roll Hall of Fame established?
A) 1985 B) 1981 C) 1983 D) 1977
""")
if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was C\n")

answer = input("""Who was the drummer for Led Zepplin?
A) Jason Bonham B) Kenny Dixon C) Neil Peart D) John Bonham
""")
if answer.lower() == "d":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was D\n")

answer = input("""This band's drummer lost his arm in a car accident:
A) Def Leppard B) Metallica C) Poison D) Journey
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
    answer = input("What was his name? ")
    if answer == "Rick Allen":
        print("Correct!\n")
        score += 1
else:
    print("Incorrect. Rick Allen was able to continue drumming for Def Leppard even after losing his arm.\n")

answer = input("""In what city was the movie Singles filmed?
A) Dallas B) Seattle C) New York D) Sacramento
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

#question 25
answer = input("""Who was the lead singer of The Doors?
A) Greg Hurts B) Roy Orbison C) Jim Morrison D) Van Morrison
""")
if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was C\n")

answer = input("""Who was the original drummer for the Melvins?
A) Dale Crover B) Coady Willis C) Mike Dillard D) None of the above
""")
if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was C\n")

answer = input("""What was the very first video released on MTV?
A) You Better Run B) Video Killed the Radio Star C) She Won't Dance Withe Me D) You Better You Bet
""")
if answer.lower() == "":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

answer = input("""What was Dave Grohl's band after Nirvana?
A) Pearl Jam B) Foo Fighters C) Nirvana D) Red Hot Chili Peppers
""")
if answer.lower() == "b\n":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

answer = input("""Approximately how many artists/bands are inducted to the Rock and Roll Hall of Fame each year? 
A) 2-3 B) 5-7 C) 9-10 D) More than 10 
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

answer = input("""In what year did Screaming Trees' bass guitarist pass away?
A) 2021 B) 2023 C) 2017 D) 2019
""")
if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was B\n")

answer = input("""Do the Red Hot Chilli Peppers have a star on Hollywood Boulevard?
y = yes | n = no
""")
if answer.lower() == "y":
    print("Correct!")
    score += 1
    answer = input("""In what year was the star unveiled?
    A) 2016 B) 2011 C) 2015 D) 2012
    """)
    if answer.lower() == "d":
        print("Correct!\n")
        score += 1
else:
    print("Incorrect! Their star was unveiled in 2012\n")

answer = input("""What album was the song Back in the USSR featured on?
A) White Album B) Abbey Road C) Let It Be D) Revolver
""")
if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was A\n")







final_score = float(score/25 * 100)
print("You got", str(final_score) + "%", "of answers correct\n")
if final_score <= float(59):
    print("You failed. Go listen to some music!\n")
elif final_score <= float(89):
    print("You passed!\n")
elif final_score <= float(99):
    print("Good job! You have aced this quiz!\n")
else:
    print("You have mastered this quiz\n")

