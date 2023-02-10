from scratch import double_characters

questions = ["What is a candy bar"]
correct_answers = ["a", "b", "c,", "d"]

score = 0
def add_score(score):
    score += 1


def ask(questions):
    answer = input(questions)
    if answer == correct_answers[0]:
        print("Correct!\n")
        add_score
    else:
        print("Incorrect! The correct answer was", correct_answers[0])

ask(questions[0])

print(double_characters("Tree"))




