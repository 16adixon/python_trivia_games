questions = ["What is a candy bar"]
correct_answers = ["a", "b", "c,", "d"]
score = 0

def ask(questions):
    score = 0
    answer = input(questions)
    if answer == correct_answers[0]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer was", correct_answers[0])

ask(questions[0])

print("Your score:", score)


