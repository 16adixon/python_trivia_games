print("\n" * 5)
print("""---------------------------
WELCOME TO LEWISTON TRIVIA!
---------------------------
""")
score = 0
questions = [

"""What year was Lewiston founded?
A) It wasn't B) 1844 C) 1901 D) 1861\n""",

"""Who bought out Potlatch?
A) Vista Outdoor B) Schweitzer Engineering C) Wal Mart D) Clearwater Paper\n""",

"""What is the elevation of the LC Valley?
A) 745' B) 650' C) 900' D) None of the above\n""",

"""What is Idaho known as?
A) The Potato State B) The Evergreen State C) The Gem State D) Nowhere to go State\n""",

"""What river runs through our valley? 
A) The Colombia River B) The FET River C) The Snake River D) Crymea River\n""",

"""What is the population Clarkston?
A) 30,056 B) 15,364 C) 7,194 D) 10,972\n""",

"""What was Idaho's first capital?
A) Nampa B) Boise C) Caldwell D) None of the above\n"""



]

correct_answers = [ "a", "b", "c", "d"]


answer = input(questions[0])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[1])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

answer = input(questions[2])
if answer == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[3])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[4])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[5])
if answer == correct_answers[2]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[2] + "\n")

answer = input(questions[6])
if answer == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

print("You got " + str(score/7 * 100) + "%", "of answers correct")
