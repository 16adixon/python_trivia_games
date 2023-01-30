print("\n" * 5)
print("""-----------------------
WELCOME TO ROCK TRIVIA!
-----------------------
""")

score = 0

questions = [

#0
"""What is Eddie Money's real name?
A) Greg Wilson B) Eddie Mahoney C) Eddie Money D) None of the Above\n""",

#1
"""Who was Iron Maidnen's original singer?
A) Bill Ward B) John Elton C) Synyster Gates D) Paul DiAnno\n""",

#2
"""Who was the drummer for Fleetwood Mac?
A) Rick Fleetwood B) Mac Fleetwood C) Mick Fleetwood D) Kenny Golladay\n""",

#3
"""What year did Black Sabath's album Masters of Reality come out?
A) 1973 B) 1978 C) 1972 D) None of the Above\n""",

#4
"""What does ELO stand for?
A) Enormous Light Organization B) Electric Light Orchestra C) Electriciy Limits Orders D) Excercise Loves Output\n""",

#5
"""What band was Don Henley the lead singer of?
A) The Eagles B) Blue Oyster Cult C) Def Leppard D) The Cure\n""",

#6
"""Who was known as the leader of Motley Crue?
A) Nikki Sixx B) Tommy Lee C) Mick Mars D) Vince Neil\n""",

#7
"""Who was the guitarist for Rush?
A) Steve Perry B) Kenny Greg C) Eddie Stixx D) Alex Lifeson\n""",

#8
"""What branch of the military was Jimmi Hendrix a part of?
A) Marines B) Navy C) Air Force D) Army\n""",

#9
"""In what city in the state of New York was Woodstock held?
A) Albany B) Buffalo C) Bethel D) None of the above\n""",

#10
"""What does WHAM stand for?
A) Wife Hates all Men B) We Hate Andrew's Mother C) What Happened at Midnight D) None of the Above\n""",

#11
"""What city was famous guitarist Slash born in
A) Hampstead B) Paris C) Lyon D) Unknown\n""",

#12
"""Who was the original lead singer of Black Sabbath
A) Ronnie James Dio B) Ozzy Osbourne C) Ian Gillian D) Ray Gillen\n""",

#13
"""David Lee Roth was also know as: _____
A) Diamond Dave B) Dynamite Dave C) Super Dave D) Dyslexic Dave\n""",

#14
"""This famous guitarist was tragically killed in a helicopter accident on August 27, 2018
A) Greg Wilson B) Stevie Ray Vaughn C) Kobe Bryant D) Randy Rhoads\n""",

#15
"""In what Super Bowl did Prince perform the halftime show?
A) Super Bowl XL B) Super Bowl XLI C) Super Bowl XLII D) Super Bowl XLIV\n""",

#16
"""What is the best selling album of all time? (As of January 25, 2023)
A) Rumours B) Thriller C) The Wall D) The Beatles(Self Titled)\n""",

#17
"""When was the Rock and Roll Hall of Fame established?
A) 1985 B) 1981 C) 1983 D) 1977\n""",

#18
"""Who was the drummer for Led Zepplin?
A) Jason Bonham B) Kenny Dixon C) Neil Peart D) John Bonham\n""",

#19
"""This band's drummer lost his arm in a car accident:
A) Def Leppard B) Metallica C) Poison D) Journey\n""",

#20
"What is his name? \n",

#21
"""In what city was the movie Singles filmed?
A) Dallas B) Seattle C) New York D) Sacramento\n""",

#22
"""Who was the original drummer for the Melvins?
A) Dale Crover B) Coady Willis C) Mike Dillard D) None of the above\n""",

#23
"""What was the very first video released on MTV?
A) You Better Run B) Video Killed the Radio Star C) She Won't Dance Withe Me D) You Better You Bet\n""",

#24
"""What was Dave Grohl's band after Nirvana?
A) Pearl Jam B) Foo Fighters C) Nirvana D) Red Hot Chili Peppers\n""",

#25
"""Approximately how many artists/bands are inducted to the Rock and Roll Hall of Fame each year? 
A) 2-3 B) 5-7 C) 9-10 D) More than 10\n""",

#26
"""In what year did Van Conner, Screaming Trees' bass guitarist, pass away?
A) 2021 B) 2023 C) 2017 D) 2019\n""",

#27
"""Do the Red Hot Chilli Peppers have a star on Hollywood Boulevard? Please type your answer.
y = yes | n = no\n""",

#28
"""In what year was the star unveiled?
A) 2016 B) 2011 C) 2015 D) 2022\n"""

]

correct_answers = ["a", "b", "c", "d"]

answer = input(questions[0])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[1])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[2])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[3])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[4])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[5])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[6])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[7])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[8])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[9])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[10])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[11])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[12])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[13])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[14])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[15])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[16])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[17])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[18])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[19])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
    answer = input(questions[20])
    if answer.lower() == "rick allen":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! It was Rick Allen\n")
else:
    print("Incorrect! Rick Allen was able to drum for Def Leppard even after losing his arm.\n")

answer = input(questions[21])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[22])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[23])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[24])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[25])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[26])
if answer == correct_answers[1]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[1] + "\n")

answer = input(questions[27],)
if answer.lower() == "yes":
    print("Correct!\n")
    score += 1
    answer = input(questions[28])
    if answer == correct_answers[3]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer was", correct_answers[3] + "\n")
else:
    print("Incorrect! They do have a star! It was unveiled in 2022!\n")

final_score = float(score/28 * 100)
print("You got", str(final_score) + "%", "of answers correct\n")
if final_score <= float(59):
    print("You failed. Go listen to some music!\n")
elif final_score <= float(89):
    print("You passed!\n")
elif final_score <= float(99):
    print("Good job! You have aced this quiz!\n")
else:
    print("You have mastered this quiz\n")


