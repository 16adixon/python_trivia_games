print("\n" * 15)
print("Welcome to LC Valley Trivia.")
playing = input("Type y to play\n")
if playing != "y":
    print("Good luck!\n")

score = 0

answer = input("""What year was Lewiston founded?
A) It wasn't B) 1844 C) 1901 D) 1861
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is D")

answer = input("""Who bought out Potlatch?
A) Vista Outdoor B) Schweitzer Engineering C) Wal Mart D) Clearwater Paper
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is D")

answer = input("""What is the elevation of the LC Valley?"
A) 745' B) 650' C) 900' D) None of the above
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was A")

answer = input("""What is Idaho known as?
A) The Potato State B) The Evergreen State C) Gem State D) Nowhere to go State
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was C")

answer = input("""What river runs through our valley? 
A) The Colombia River B) The FET River C) The Snake River D) Crymea River
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was C")

answer = input("""What is the population Clarkston?
A) 30,056 B) 15,364 C) 7,194 D) 10,972
""")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer was C")

answer = input("""What was Idaho's first capital?
A) Nampa B) Boise C) Caldwell D) None of the above
""")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Lewiston was the first capital of Idaho")




