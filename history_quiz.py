print("History Quiz")

score = 0

playing = "Press y to play"
if playing.lower() != "y":
    print("Good Luck!")
else:
    print("FUCK YOU!")
    quit()

correct_answers = ['a', 'b', 'c', 'd']

questions = [

#[0] correct answer is a
"""What year did World War II end?
A) 1945 B) 1943 C) 1948 D) 1950
""",

#[1] correct answer is d
"""Who was the 45th President of the United States?
A) Bill Clinton B) Barrack Obama C) George Bush Jr. D) Donald Trump
"""

]

answer = input(questions[0])
if answer.lower() == correct_answers[0]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[0] + "\n")

answer = input(questions[1])
if answer.lower() == correct_answers[3]:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was", correct_answers[3] + "\n")

